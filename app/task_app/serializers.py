from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ['url', 'title', 'description', 'date_create', 'status', 'expected_dead_line']



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',  'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
