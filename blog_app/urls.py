from django.conf.urls import url
from django.urls import path
from blog_app import views

app_name = "blog_app"

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:slug>', views.blog_details, name='blog_details'),

]