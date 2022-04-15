from django.db import models
from accounts.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=250)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"""
        ID: {self.id}
        Task: {self.name}
        Completed: {self.is_complete}
        """
