from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.generics import *
from django.contrib.auth.models import User


class TaskUserListView(ListAPIView):

    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.filter(user=User)
        return queryset