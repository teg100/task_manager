from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tasks', TaskUserView, basename='task')

urlpatterns = [
    path('', include(router.urls))
]
