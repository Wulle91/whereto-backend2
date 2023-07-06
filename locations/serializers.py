from rest_framework import serializers
from .models import Location
from follow_locations.models import FollowLocation


class LocationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()
    is_following = serializers.SerializerMethodField()

    def get_location(self, obj):
        request = self.context['request']
        return FollowLocation.objects.filter(
            owner=request.user, followed_location=obj).exists()

    def get_is_following(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            following = FollowLocation.objects.filter(
                owner=user, followed_location=obj.owner
            ).first()
            return following.id is not None
        return False

    class Meta:
        model = Location
        fields = [
            'id', 'name', 'address', 'followers_count', 'posts_count',
            'image_url', 'is_following', 'address'
        ]
