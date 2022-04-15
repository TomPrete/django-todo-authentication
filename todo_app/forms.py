from .models import Task
from django.forms import ModelForm
# Create your views here.

class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'is_complete']
