from urllib.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import models, serializers
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from profile_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
class HelloApiView(APIView):
    '''Test API views'''
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """return a list if APIView feacture"""
        an_apiviews={
        "uses Http methods as function(get,post,patch,put,delete)",
        "is similar to traditional django views",
        "gives you most control over your application logos",
        "is mapped manually to urls",
        }
        return Response({"message":"hello","an_apiviews":an_apiviews})

    def post(self,request):
        """ create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            message=f"hello {name}"

            return Response({"message":message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """Handle updating a object"""
        return Response({"method":"PUT"})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({"method":"PATCH"})

    def delete(self,request,pk=None):
        """delete of an object"""
        return Response({"method":"DELETE"})

class helloviewset(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class=serializers.HelloSerializer

    def  list(self,request):
        """return a hello message"""

        a_viewset={
            'uses actions (list,create,retrive,update,partial_update)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code',
        }

        return Response({'message':'hello','a_viewset':a_viewset})


    def create(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})


    def update(self,request,pk=None):
        """Handle update object by its ID"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle partial object by its object"""
        return Response({"http_method":'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':"DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES





