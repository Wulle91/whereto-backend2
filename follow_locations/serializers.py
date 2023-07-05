from django.db import IntegrityError
from rest_framework import serializers
from .models import FollowLocation


class FollowLocationSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_location = serializers.ReadOnlyField(
        source='followed_location.name')

    class Meta:
        model = FollowLocation
        fields = [
            'id', 'owner', 'created_at', 'followed_name', 'followed_location'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
