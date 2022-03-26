from dataclasses import field, fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainapp.models import Games

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Games
        fields = ['black', 'white']