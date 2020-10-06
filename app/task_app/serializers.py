from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'date_create', 'status', 'expected_dead_line']
