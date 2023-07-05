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
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed', 'followed_location']

    def __str__(self):
        return f'{self.owner} {self.followed}'


def followers_pre_save(sender, instance, *args, **kwargs):
    if instance.followed is None:
        random_user = User.objects.order_by('?').first()
        instance.followed = random_user
    if instance.followed_location is None:
        random_location = Location.objects.order_by('?').first()
        instance.followed_location = random_location


pre_save.connect(followers_pre_save, sender=Follower)
