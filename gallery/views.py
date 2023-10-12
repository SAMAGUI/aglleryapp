from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

from gallery import models
from gallery.forms import AlbumDetailForm, AlbumForm, PhotoForm


def home(request):
    banners = models.Banners.objects.all()
    return render(request, "home.html", {'banners': banners})


@login_required(login_url='login')
def gallery(request):
    gallery = models.Photo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'gallery.html', {'gallerys': gallery})


@login_required(login_url='login')
def albums(request):
    albums = models.Album.objects.filter(user=request.user).order_by('-id')
    return render(request, 'album.html', {'albums': albums})


@login_required(login_url='login')
def addphoto(request):
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            print(instance)
            return redirect("gallery")
    context = {
        'form': form
    }
    return render(request, "createphoto.html", context)


@login_required(login_url='login')
def addalbum(request):
    form = AlbumForm()
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            print(instance)
            return redirect("albums")
    context = {
        'form': form
    }
    return render(request, "newalbum.html", context)


@login_required(login_url='login')
def album_detail(request, id):
    album = models.Album.objects.get(id=id)
    details = models.AlbumDetail.objects.filter(album=album)
    return render(request, 'album-detail.html', {'details': details, 'album': album})


@login_required(login_url='login')
def add_image(request, id):
    form = AlbumDetailForm()
    album = models.Album.objects.get(id=id)
    if request.method == "POST":
        form = AlbumDetailForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.album = album
            instance.save()
            print(instance)
            return redirect("add-image", id=album.id)
    context = {
        'form': form
    }
    return render(request, "add-image.html", context)

@login_required()
def delete_photo(request, id):
    photo = get_object_or_404(models.Photo, id=id)
    if request.method == 'POST':
        photo.delete()
        return redirect("gallery")
    return render(request, 'delete-photo.html')

@login_required()
def delete_image(request, id):
    detail = get_object_or_404(models.AlbumDetail, id=id)
    album = get_object_or_404(models.Album, id=detail.album.id)
    if request.method == 'POST':
        detail.delete()
        return redirect("album-detail", id=album.id)
    return render(request, 'delete-image.html', {'album': album})
