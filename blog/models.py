from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    update_post = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title