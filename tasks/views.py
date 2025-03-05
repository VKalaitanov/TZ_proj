from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    """
    API-вью для получения списка задач (GET) и создания новой задачи (POST).
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer