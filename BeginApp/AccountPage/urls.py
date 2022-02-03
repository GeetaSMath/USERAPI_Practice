from idlelib.multicall import r

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user_registration/', views.UserRegistration.as_view(), name='user_registration'),
    re_path(r'^user_registration/(?P<username>[\w0-9-]+)/$', views.UserRegistration.as_view(),name='user_registration'),
]
