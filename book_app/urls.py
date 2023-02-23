# from django.conf.urls import url
from django.urls import path
from book_app import views

app_name = "book_app"

urlpatterns = [
    path('', views.book, name='book'),

]