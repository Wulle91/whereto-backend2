from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from locations.models import Location


def validate_follow_uniqueness(value):
    owner = value.owner
    followed = value.followed
    followed_location = value.followed_location

    # Check if either 'followed' or 'followed_location' is unique for the owner
    if Follower.objects.filter(owner=owner).filter(models.Q(followed=followed) | models.Q(followed_location=followed_location)).exists():
        raise ValidationError("A unique follow relationship already exists for the owner.")


class Follower(models.Model):
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE, null=True
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE, null=True, blank=True
    )
    followed_location = models.ForeignKey(
        Location, related_name='followers', on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.followed}'

    def clean(self):
        validate_follow_uniqueness(self)
