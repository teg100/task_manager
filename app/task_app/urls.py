from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'tasks', TaskUserView, basename='task')

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user-login'),
    path('register/', UserCreate.as_view(), name='account-create'),
    path('tasks/<int:id>/history/', HistoryTaskView.as_view(), name='history-task'),
    path('', include(router.urls))
]
