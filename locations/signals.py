from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Post
from .models import Location


@receiver(post_save, sender=Post)
def create_location(sender, instance, created, **kwargs):
    if created:
        Location.objects.get_or_create(
            name=instance.name,
            address=instance.address,
            image_url=instance.image_url
        )
