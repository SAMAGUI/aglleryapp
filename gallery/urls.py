from django.urls import path

from gallery import views


urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('gallery/add/', views.addphoto, name="add-photo"),
    path('gallery/<int:id>/', views.delete_photo, name="delete-photo"),
    path('albums/', views.albums, name="albums"),
    path('albums/add/', views.addalbum, name="add-album"),
    path('albums/<int:id>/add-image/', views.add_image, name="add-image"),
    path('albums/<int:id>/', views.album_detail, name="album-detail"),
    path('albums/<int:id>/delete/', views.delete_image, name="delete-image"),
]