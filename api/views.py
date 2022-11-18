from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
import requests
from django.contrib.auth.models import User


success = {'code':status.HTTP_200_OK,'message':'success'}
no_argument = {'code':status.HTTP_400_BAD_REQUEST,'message':'no required parameter found'}
failed = {'code':status.HTTP_400_BAD_REQUEST,'message':'failed'}

class MoviesList(viewsets.ViewSet):
    def list(self , request):
        response = requests.get(f"https://demo.credy.in/api/v1/maya/movies/")
        context = {
        "Message": success,
            "Output":response.json()
         }
        return Response(context)


class Register(viewsets.ViewSet):
    def create(self , request):
        data = request.data
        if not User.objects.filter(username = data['username']):
            user = User.objects.create_user(username=data['username'],
                                        password=data['password'])
            output = "User successfully registered"
            message = success
        else:
            output = "User Already Registered"
            message = failed
        context = {
        "Message": message,
        "Output":output
         }
        return Response(context)


class Collection(viewsets.ViewSet):
    def create(self , request):
        data = request.data

        response = requests.get(f"https://demo.credy.in/api/v1/maya/movies/")

        output = response.json()
        for res in output['results']:

            if res["uuid"] == data['uid']:
                print(res)
                output = res


        context = {
        "Message": success,
        "Output":output
         }
        return Response(context)