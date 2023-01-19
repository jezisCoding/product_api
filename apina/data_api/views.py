from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import my_models
from .serializers import my_serializers

# Create your views here.

class DeleteView(APIView):
    def delete(self, request, *args, **kwargs):
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
            if serializer.is_valid():
                serializer.save()
            else:
                print('ser error items')
                print(serializer.errors.items())
                # if id error
                if 'id' in serializer.errors.keys():
                    print('type:')
                    print(type(serializer.errors['id'][0]))
                    print('dir:')
                    print(dir(serializer.errors['id'][0]))
                    print('attempt:')
                    err_code = serializer.errors['id'][0].code
                    # if unique id error, its not an error.  we update
                    if err_code == 'unique':
                        #get item with given id
                        print('ser data:')
                        print(serializer.data['id'])
                        model = my_models[model_name]
                        item = model.objects.get(id=serializer.data['id'])
                        print('item:')
                        print(item)
                        #add smth to it (attr=attr)
                        print('ser data:')
                        print(serializer.data)
                        for key in serializer.data:
                            if not hasattr(item, key):
                                setattr(item, key, serializer.data[key])
                                # thiss only adds attribute if it wasnt there
                                # i think i just shouldnt hasattr otherwise
                        print('save now for what')
                        model.objects.save(item)
                        #save it again

                obj['errors'] = serializer.errors
                response_data = { 'object': obj }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        # Respond with what was created
        return Response(request.data, status=status.HTTP_201_CREATED)

class ModelNameListView(APIView):
    def get(self, request, model_name, *args, **kwargs):
        '''
        Return a response with all objects of model_name
        '''
        
        try:
            data = my_models[model_name].objects
        except KeyError:
            return Response(
                    data=("Model {} does not exist".format(model_name)),
                    status=status.HTTP_400_BAD_REQUEST
                    )

        serializer = my_serializers[model_name](data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModelNameIdView(APIView):
    def get(self, request, model_name, id, *args, **kwargs):
        '''
        Return a response with data by model_name and id
        '''
        model = my_models[model_name]
        data = None

        try:
            data = model.objects.get(id=id)
        except model.DoesNotExist:
            return Response(
                {"res": "Object {model_name} with id {id} does not exist".format(
                    model_name=model_name, id=id)},
                status=status.HTTP_400_BAD_REQUEST)

        serializer = my_serializers[model_name](data)
        return Response(serializer.data, status=status.HTTP_200_OK)
