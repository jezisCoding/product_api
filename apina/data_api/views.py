from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# testing import
from operator import itemgetter

from .models import my_models
from .serializers import my_serializers

# Create your views here.

class DeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        '''
        Delete all rows in all model tables
        '''
        response_data = []
        for m in my_models.keys():
            deleted = my_models[m].objects.all().delete()
            response_data.append(deleted)
            print("deleted {}".format(deleted))
        return Response(response_data, status=status.HTTP_202_ACCEPTED)

class ImportView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Insert request data into database. Keep inserting until error in data. 
        When error found, return object with its error.
        '''
        for obj in request.data:
            model_name = list(obj.keys())[0]
            serializer = my_serializers[model_name](data=obj[model_name])

            if not serializer.is_valid():
                obj['errors'] = serializer.errors
                response_data = { 'object': obj }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            else:
                model = my_models[model_name]
                item = model.objects.filter(pk=serializer.validated_data['id'])
                # a povieme vsetkym ze maju ignorovat unique id validator

                # dostane sa sem kod vobec niekedy? nevyhodi to vyssie 
                # uz exception KeyError? 
                # mozno ho tam chytit radsi
                if item:
                    print('updating with object:')
                    print(serializer.validated_data)
                    # Update reportedly does not send signals to other apps
                    # We only have one app so I am using it here
                    item.update(**serializer.validated_data)
                else:
                    serializer.save()
                    #return Response(
                    #        data=("Model {} does not exist".format(model_name)),
                    #        status=status.HTTP_400_BAD_REQUEST
                    #        )
                
        # All sucessful. Respond with what was created
        return Response(request.data, status=status.HTTP_201_CREATED)

class ModelNameListView(APIView):
    def get(self, request, model_name, *args, **kwargs):
        '''
        Return a response with all objects of model_name
        '''
        
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
        '''
        Return a response with object by model_name and id
        '''
        model = my_models[model_name]

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
