import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Follower
from locations.models import Location


@receiver(post_save, sender=Follower)
def populate_missing_fields(sender, instance, created, **kwargs):
    if created:
        if not instance.followed:
            random_user = User.objects.order_by('?').first()
            instance.followed = random_user

        if not instance.followed_location:
            random_location = Location.objects.order_by('?').first()
            instance.followed_location = random_location

        instance.save()