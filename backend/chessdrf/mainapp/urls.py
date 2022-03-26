from django.urls import path
from . import views

urlpattrens = [
    path('user/',views.UserViewSet,name="UserViewSet"),
    path('group/',views.GroupViewSet,name="GroupViewSet"),
    path('game/',views.GameViewSet,name="GameViewSet"),
]