from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    text = models.TextField()
    
    def __str__(self):
        return self.title
