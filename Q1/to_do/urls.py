from django.urls import path
from .views import TaskList,TaskUpdate

urlpatterns = [
    path('api',TaskList.as_view()),
    path('api/<int:id>',TaskUpdate.as_view())
]