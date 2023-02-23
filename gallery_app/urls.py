# from django.conf.urls import url
from django.urls import path
from gallery_app import views

app_name = "gallery_app"

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<slug:slug>/', views.GalleryDetailView.as_view(), name='gallery_details'),

]