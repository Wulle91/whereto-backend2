from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Post
from .models import Location


@receiver(post_save, sender=Post)
def create_location(sender, instance, created,
                    image, owner, created_at, **kwargs):
    if created:
        location, _ = Location.objects.get_or_create(
            name=instance.name,
            address=instance.address,
            image_url=instance.image_url
        )

        Post.objects.create(
            title=instance.title,
            content=instance.content,
            name=instance.name,
            address=instance.address,
            image=instance.image,
            owner=instance.owner,
            created_at=instance.created_at
        )
