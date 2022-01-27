from django.db import models


class User(models.Model):
    """
    created this class for table in database
    """
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


