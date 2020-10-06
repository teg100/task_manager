from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404


class UserLogin(APIView):
    """
        Login user

        :parameters: username, password
        :return: token
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)


class TaskUserView(viewsets.ModelViewSet):
    """
        CRUD operations for task
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'expected_dead_line']

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HistoryTaskView(APIView):
    """
        List history for task
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        task = get_object_or_404(Task, id=id, user=request.user)
        if task:
            serializer = HistoryTaskSerializer(task.history.all(), many=True)
            return Response(serializer.data, status=HTTP_200_OK)


class UserCreate(APIView):
    """
        Creates the user.

        :parameters: username, password
        :return: token
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = {'token': token.key}
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)