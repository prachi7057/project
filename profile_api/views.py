from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


class HelloApiVIew(APIView):

    def get(self, request, format=None):

        an_api = [

        "Uses Statndard HTTP methods as function(get, post,put,delete)",

        "It is similar to traditional Django view",

        "Gives you control over ur application and logic",

        "It mapped manually to URL's"

        ]


        return Response({"message":"hello world", "an_api" : an_api})


    serializer_class = serializers.HelloSerializers
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        print('Log for serializer',type(serializer))
        if serializer.is_valid():
            name=serializer.validated_data.get("name")

            age=serializer.validated_data.get("age")

            message = f"hello {name, age}"

            return Response({'message' : message})

        else:

            return Response(serializer.errors,

            status = status.HTTP_400_BAD_REQUEST

            )



    def put(self, request, pk=None):

        """Handling update an object"""

        return Response({'method':'PUT'})


    def patch(self, request, pk=None):

        """Handling partial update of an object """

        return Response({'method' : 'PATCH'})


    def delete(self, request,pk=None):

        """Delete an Object """

        return Response({'method' : 'DELETE'})
