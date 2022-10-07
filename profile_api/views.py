from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    '''Test API views'''

    def get(self,request,format=None):
        """return a list if APIView feacture"""
        an_apiviews={
        "uses Http methods as function(get,post,patch,put,delete)",
        "is similar to traditional django views",
        "gives you most control over your application logos",
        "is mapped manually to urls",
        }
        return Response({"message":"hello","an_apiviews":an_apiviews})
