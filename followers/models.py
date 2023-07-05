from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from locations.models import Location


class Follower(models.Model):
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE,
        null=True
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE,
        null=True
    )
    followed_location = models.ForeignKey(
        Location, related_name='followers',
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = [
            ('owner', 'followed'),
            ('owner', 'followed_location'),
        ]

    def __str__(self):
        return f'{self.owner} {self.followed}'
