from django.db import models
from users.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title  = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    