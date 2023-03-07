from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import my_models
from .serializers import my_serializers

# Create your views here.

class DeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        """
        Delete all rows in all model tables.
        Intended for debugging.
        """
        response_data = []
        for m in my_models.keys():
            deleted = my_models[m].objects.all().delete()
            response_data.append(deleted)
            print("deleted {}".format(deleted))
        return Response(response_data, status=status.HTTP_202_ACCEPTED)

class ImportView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Insert request data into database. If id already in database, update.
        Keep working until error in data. When error found, return object 
        with its error. All data until error object is saved.

        TODO hopefully working correctly. I havent tested all outputs.

        HTTP Codes
            - 201 = All data saved
            - 400 = Bad data in input data, all data until then saved
        """
        for obj in request.data:
            model_name = list(obj.keys())[0]
            model = my_models[model_name]

            try:
                item = model.objects.get(pk=obj[model_name]['id'])
                # if we give item (instance) param then save() does update()
                serializer = my_serializers[model_name](item, data=obj[model_name])
            except model.DoesNotExist:
                # else save() does create()
                serializer = my_serializers[model_name](data=obj[model_name])

            if not serializer.is_valid():
                obj['errors'] = serializer.errors
                response_data = { 'object': obj }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            else:
                serializer.save()
                
        # All successful. Respond with what was created
        return Response(request.data, status=status.HTTP_201_CREATED)

class ModelNameListView(APIView):
    def get(self, request, model_name, *args, **kwargs):
        """
        Return a response with all objects of model_name

        HTTP Codes
            - 200 = Success
            - 400 = Model does not exist
        """
        
        try:
            objs = my_models[model_name].objects
        except KeyError:
            return Response(
                    data=("Model {} does not exist".format(model_name)),
                    status=status.HTTP_400_BAD_REQUEST
                    )

        # we give this to serializer to push it through to_representation()
        serializer = my_serializers[model_name](objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModelNameIdView(APIView):
    def get(self, request, model_name, id, *args, **kwargs):
        """
        Return a response with object by model_name and id

        HTTP Codes
            - 200 = Success
            - 400 = Id does not exist
        """
        try:
            model = my_models[model_name]
        except KeyError:
            return Response(
                    data=("Model {} does not exist".format(model_name)),
                    status=status.HTTP_400_BAD_REQUEST
                    )

        try:
            obj = model.objects.get(id=id)
        except model.DoesNotExist:
            return Response(
                {"res": "Object {model_name} with id {id} does not exist".format(
                    model_name=model_name, id=id)},
                status=status.HTTP_400_BAD_REQUEST
                )

        # we give this to serializer to push it through to_representation()
        serializer = my_serializers[model_name](obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
