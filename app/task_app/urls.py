from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskUserListView.as_view(), name='_task_list_view')
]
