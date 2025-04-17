from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissioons.IsAuthenticared]
    filter_backends = [filter.SearchFilter, filter.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        self.get_queryset().delete()
        return Response({"message": "Все задачи удалены"})  
    
    