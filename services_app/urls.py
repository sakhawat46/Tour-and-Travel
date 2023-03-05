# from django.conf.urls import url
from django.urls import path
from services_app import views

app_name = "services_app"

urlpatterns = [
    path('', views.services, name='services'),
    path('visa/', views.visa, name='visa'),
    path('visa_details/', views.visa_details, name='visa_details'),

]