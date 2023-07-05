from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from whereto.permissions import IsOwnerOrReadOnly
from .models import Location
from .serializers import LocationSerializer


class LocationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Location.objects.annotate(
        posts_count=Count('name', distinct=True),
    ).order_by('-created_at')
    serializer_class = LocationSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'name',
        'address',
    ]
    ordering_fields = [
        'posts_count',
        'name',
        'followers_count',
    ]


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Location.objects.annotate(
        posts_count=Count('name', distinct=True),
        # followers_count=Count('name__followed', distinct=True),
    ).order_by('-created_at')
    serializer_class = LocationSerializer
