from django.conf.urls import url
from django.urls import path
from home_app import views

app_name = "home_app"

urlpatterns = [
    path('', views.home, name='home'),

]