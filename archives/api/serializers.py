from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from archives.models import ArchivePost

User = get_user_model()


class ArchivePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArchivePost
        fields = ('id',
                  'title',
                  'image',
                  'description',
                  'created',
                  'updated',)
