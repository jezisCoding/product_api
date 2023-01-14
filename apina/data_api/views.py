from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import myModels
from .serializers import mySerializers

# Create your views here.

class ImportView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        Insert request data into database.
        First check if all data valid. Then save and send response.
        '''
        for obj in request.data:
            print('data object:')
            print(obj)
            modelName = list(obj.keys())[0]
            serializer = mySerializers[modelName](data=obj[modelName])
            if not serializer.is_valid():
                responseData = { 'object': obj, 'errors': serializer.errors }
                return Response(responseData, status=status.HTTP_400_BAD_REQUEST)
            
        # Everything is ok. Let's save 
        #responseData = []
        for obj in request.data:
            modelName = list(obj.keys())[0]
            serializer = mySerializers[modelName](data=obj[modelName])
            if serializer.is_valid():
                print('serializer data2:')
                print(serializer.validated_data)
                serializer.save()
                #responseData.append(serializer.validated_data)

        return Response(request.data, status=status.HTTP_201_CREATED)

class ModelNameListView(APIView):
    def get(self, request, model_name, *args, **kwargs):
        '''
        Return a response with all objects of model_name
        '''
        
        data = myModels[model_name].objects
        serializer = mySerializers[model_name](data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModelNameIdView(APIView):
    def get(self, request, model_name, id, *args, **kwargs):
        '''
        Return a response with data by model_name and id
        '''
        model = myModels[model_name]
        data = None

        try:
            data = model.objects.get(id=id)
        except model.DoesNotExist:
            return Response(
                {"res": "Object {model_name} with id {id} does not exist".format(
                    model_name=model_name, id=id)},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = mySerializers[model_name](data)
        return Response(serializer.data, status=status.HTTP_200_OK)
