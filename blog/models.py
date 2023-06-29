from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length = 500, null=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(timezone.now())
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title