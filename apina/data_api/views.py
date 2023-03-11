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
        Insert request data into database.

        HTTP Codes
            - 200 = Data created or updated
            - 400 = Bad data in input data, all data until then is saved
        """
        
        if type(request.data) == dict:
            model_name = list(request.data.keys())[0]

            try:
                model = my_models[model_name]
            except KeyError:
                return Response(
                        "Model {} does not exist in database".format(model_name),
                        status=status.HTTP_400_BAD_REQUEST
                        )

            r = self.save_object(model, request.data)
            print('aaa')
            print(r)
            return Response(r, status=status.HTTP_200_OK)

        elif type(request.data) == list:
            for obj in request.data:
                r = self.save_object(obj)
                print(r)

    def save_object(self, model, obj):
        """
        Save an object into database. If id already in database, update.
        Keep working until error in data. When error found, return object 
        with its error. All data until error object is saved.

        TODO hopefully working correctly. I havent tested all outputs.
        """
        model_name = model.__name__

        try:
            item = model.objects.get(pk=obj[model_name]['id'])
            # if we give item (instance) param then save() does update()
            serializer = my_serializers[model_name](item, data=obj[model_name])
        except model.DoesNotExist:
            # else save() does create()
            serializer = my_serializers[model_name](data=obj[model_name])

        serializer.is_valid(raise_exception=True)
        if not serializer.is_valid():
            obj['errors'] = serializer.errors
            response_data = { 'object': obj }
            raise INVALID_DATA
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        else:
            # TODO returns None if saved nothing (and updated nothing? try)
            saved_object = serializer.save()
            print(saved_object)
            return saved_object

        # WIP neni to to vubec doriesene, treba to zjednotit asi, nemozem len tak hadzat kody alebo 
        # responzy


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
        print(my_models[model_name])
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
