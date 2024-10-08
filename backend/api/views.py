from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)  # fujiokpl
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskBbiew(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(name='nn')

    def update(self, request):
        pass
