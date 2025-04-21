from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter 
from django.http import HttpResponse

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]  
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
