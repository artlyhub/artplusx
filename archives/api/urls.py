from django.conf.urls import url

from archives.api.views import ArchivePostAPIView, ArchivePostDetailsAPIView

urlpatterns = [
    url(r'^$', ArchivePostAPIView.as_view(), name='archive-post'),
    url(r'^(?P<pk>[\w.@+-]+)/$',
        ArchivePostDetailsAPIView.as_view(), name="archive-post-details"),
]
