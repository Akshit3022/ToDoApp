from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    task = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True, default="In Progress")

    def __str__(self):
        return self.task