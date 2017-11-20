from django import forms

from archives.models import ArchivePost


class ArchivePostForm(forms.ModelForm):
    class Meta:
        model = ArchivePost
        fields = ('title',
                  'image',
                  'description',)
