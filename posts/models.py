from django.db import models
from django.contrib.auth import get_user_model



class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title