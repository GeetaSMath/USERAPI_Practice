from django.http import HttpResponse
from django.contrib.auth.models import User
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
            data = User.objects.all()
            user_data = []
            for obj in data:
                user_dict = {"username": obj.username, "password": obj.password, "email": obj.email,"first_name": obj.first_name,
                             "last_name": obj.last_name}
                user_data.append(user_dict)
                return HttpResponse(user_data)
        except Exception as e:
            return HttpResponse("Raise an error"+e.__str__())


    def put (self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            user.password = request.data['password']
            user.email = request.data['email']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.save()
            return HttpResponse("data updated")
        except Exception as e:
            return HttpResponse("Raise an error"+e.__str__())

    def delete (self, request):
        """"""
        try:
            user = User.objects.get(username=request.data['username'])
            user.delete()
            return HttpResponse("User deleted successfully")
        except Exception as e:
            return HttpResponse("Raise an error"+e.__str__())
