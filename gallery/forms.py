from django import forms
from django.utils.safestring import mark_safe
from gallery.models import Album, AlbumDetail, Photo


class CustomChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return mark_safe("<img src='%s' />" % obj.file.url)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        exclude = ["user"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        exclude = ["user", "logo"]

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class AlbumDetailForm(forms.ModelForm):

    # photo = CustomChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Photo.objects.all())

    class Meta:
        model = AlbumDetail
        fields = {'photo'}        
        