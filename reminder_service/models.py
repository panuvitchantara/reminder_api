from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.


class Reminder(models.Model):
    
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # editor = models.ManyToManyField(User) 

    def __str__(self):
        return f"{self.title}"

class ShareReminder(models.Model):

    reminder = models.ForeignKey(Reminder,on_delete=models.CASCADE)
    # editor = models.ManyToManyField(Editor)

    # title = models.CharField(max_length=100)
    # status = models.CharField(max_length=100)
    # priority = models.CharField(max_length=100)
    # description = models.TextField(blank=True)
    
    # created_date = models.DateTimeField(auto_now_add=True)
    # last_modified = models.DateTimeField(auto_now=True)
    # due_date = models.DateTimeField(blank=True)

    # creator = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.editor}"



