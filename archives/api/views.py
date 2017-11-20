from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from rest_framework.views import APIView

from archives.models import ArchivePost
from archives.api.serializers import ArchivePostSerializer
# from utils.permissions import IsOwnerOrReadOnly
# from utils.paginations import UserResultPagination, StandardResultPagination

User = get_user_model()


class ArchivePostAPIView(generics.ListCreateAPIView):
    queryset = ArchivePost.objects.get_queryset()
    serializer_class = ArchivePostSerializer


class ArchivePostDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArchivePost.objects.all()
    serializer_class = ArchivePostSerializer
