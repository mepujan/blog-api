from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} created by {self.author.username}'


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{self.author} commented on post {self.blog}'
