from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.generics import *
from django.contrib.auth.models import User


class TaskUserView(viewsets.ModelViewSet):
    """
        CRUD operations for task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, validated_data):
        # validated_data['user'] = self.request.user
        return super().create(validated_data)