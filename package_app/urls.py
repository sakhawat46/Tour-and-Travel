from django.conf.urls import url
from django.urls import path
from package_app import views

app_name = "package_app"

urlpatterns = [
    path('', views.package, name='package'),
    path('<str:slug>', views.package_details, name='package_details'),

]