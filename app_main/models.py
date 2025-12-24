from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        REJECTED = 'rejected'
        APPROVED = 'approved'
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    text = models.TextField(null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(to=User,on_delete=models.SET_DEFAULT, default="unknown", null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    
    def __str__(self):
        return f"{self.title}::{self.user}"
    
    
class PostDetail(models.Model):
    pass

class MultiMedia(models.Model):
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    content = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files', null=True)
    file = models.FileField(upload_to='./post', null=True)
    
    def __str__(self):
        return f"{self.id} :: {self.content.name}"

class Comment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending'
        REJECTED = 'rejected'
        APPROVED = 'approved'

    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    content = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    text = models.TextField(null=True)

    def __str__(self):
        return f"{self.user.username}::{self.text[:8:1]}"
    

