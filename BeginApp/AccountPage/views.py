import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class UserRegistration(APIView):
    def post(self, request):

        """
        this method is created for user registration
        :param request: passing the request
        :return: outcome result
        """
        try:
            data = request.data
            user_name = data.get("user_name")
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            password = data.get("password")
            email = data.get("email")
            user = User(username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return HttpResponse("Data stored successfully")

        except Exception as e:
            print(e)
            return HttpResponse("Raise an error"+e.__str__())

    def get(self, request):
        """
        :param request:
        :return:
        """
        try:
            data = User.objects.get()
            print(data)
            Data_list=[]
            for i in data:
                Data_list.append(i)
            return Data_list

        except Exception as e:
            print(e)
            return HttpResponse("Raise an error" + e.__str__())

    def delete(self, request, email, format=None):
        """"""
        try:
            data = self.get_object(email)
            data.delete()

        except Exception as e:
                print(e)
                return HttpResponse("Raise an error" + e.__str__())

