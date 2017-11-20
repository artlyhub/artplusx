from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic.detail import DetailView

from archives.forms import ArchivePostForm
from archives.models import ArchivePost


class ArchivesPostView(View):
    def get(self, request):
        form = ArchivePostForm()
        archives_list = ArchivePost.objects.all()
        return render(self.request,
                      'index.html',
                      {
                        'archives': archives_list,
                        'form': form
                      })

    def post(self, request):
        form = ArchivePostForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            archive = form.save()
            data = {
                'is_valid': True,
                'title': archive.title,
                'url': archive.image.url,
                'description': archive.description
            }
        else:
            data = {'is_valid': False}
        print(data)
        return JsonResponse(data)


class ArchivePostDetailView(DetailView):
    model = ArchivePost

    def get_context_data(self, **kwargs):
        pass
