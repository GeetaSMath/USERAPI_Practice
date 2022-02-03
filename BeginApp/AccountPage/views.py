from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView

class UserRegistration(APIView):
    def post(self, request):
        """
        post method to add userdata
        :param request:
        :return:
        """
        try:
            data = request.data
            user = User(username=data['username'],
                      first_name=data['first_name'],
                      last_name=data['email'],
                      password=data['password'],
                      email=data['email'])
            user.save()
            return JsonResponse({"messages":"user stored"},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error":"error occured due to " +e.__str__()})



    def get(self):
        """
        get method to get information from database
        :param request:
        :return:
        """
        try:
            data = User.objects.all()
            user_data = []
            for obj in data:
                user_dict = {"username": obj.username, "password": obj.password, "email": obj.email,"first_name": obj.first_name,
                             "last_name": obj.last_name}
                user_data.append(user_dict)

            return JsonResponse({"data":user_data},status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({"error":"error occurred due to " +e.__str__()})


    def put (self, request,username):
        """
        put method to update data
        :param request:
        :param username:
        :return:
        """
        try:
            user = User.objects.get(username=username)
            user.password = request.data['password']
            user.email = request.data['email']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.save()
            return JsonResponse({"messages":"user updated"},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error":"error occurred due to " +e.__str__()})

    def delete (self, request):
        """
        delete item with username
        :param request:
        :return:
        """
        try:
            user = User.objects.get(username=request.data['username'])
            user.delete()
            return JsonResponse({"deleted user":"done"},status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({"error":"error occured due to " +e.__str__()})
