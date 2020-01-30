from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class AddList(models.Model):
    listName = models.CharField(max_length=150)

class AddTask(models.Model):
    
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    expected_time = models.TimeField(null=True)
    due_date = models.DateField(blank=True,null=True)
    status = models.IntegerField(null=True)










