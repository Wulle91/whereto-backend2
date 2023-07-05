from rest_framework import generics, permissions
from whereto.permissions import IsOwnerOrReadOnly
from .models import FollowLocation
from .serializers import FollowerSerializer


class FollowLocationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FollowLocation.objects.all()
    serializer_class = FollowLocationSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowLocationDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = FollowLocation.objects.all()
    serializer_class = FollowLocationSerializer
