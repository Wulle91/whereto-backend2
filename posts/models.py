from django.db import models
from django.contrib.auth.models import User
from locations.models import Location


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, default='')
    image_url = models.URLField(blank=True, max_length=1000, default='')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
