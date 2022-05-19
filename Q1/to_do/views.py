from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_complete']
    permission_classes = [permissions.IsAuthenticated]

class TaskUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]
