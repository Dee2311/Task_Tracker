from rest_framework import serializers
from .models import AddList,AddTask
from django.contrib.auth.models import User

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddList
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddTask
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password')