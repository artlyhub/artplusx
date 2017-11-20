import uuid

from django.db import models
from sorl.thumbnail import ImageField

def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return "archive/{}.{}".format(uuid.uuid4(), extension)


class ArchivePost(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = ImageField(upload_to=scramble_uploaded_image)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
