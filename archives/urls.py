from django.conf.urls import url

from archives.views import ArchivesPostView

urlpatterns = [
    url(r'^$', ArchivesPostView.as_view(), name="archive-post"),
]
