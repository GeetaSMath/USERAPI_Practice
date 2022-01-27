import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def user_registration(request):
    """
    this method is created for user registration
    :param request: passing the request
    :return: outcome result
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            user_name = data.get("user_name")
            password = data.get("password")
            email = data.get("email")
            user = User(user_name=user_name, password=password, email=email)
            user.save()
            return HttpResponse("Data stored successfully")
    except Exception as e:
        return "Error"

@csrf_exempt
def user_login(request):
    """
    this method is created for user_login
    :param request: web request for login
    :return:
    """
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            user_name = data["user_name"]
            password = data["password"]

            if User.objects.filter(user_name=user_name, password=password):
                return HttpResponse("User is exist")
    except Exception as e:
        return "Error"



