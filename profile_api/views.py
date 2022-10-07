from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


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
