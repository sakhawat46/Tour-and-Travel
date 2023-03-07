from django.db import models
from django.forms import IntegerField
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Packages(models.Model):
    tour_place = models.CharField(max_length=255, verbose_name='Enter Tour Place')
    tour_place_description = RichTextField()
    packages_image = models.ImageField(upload_to='packages_images', verbose_name='Image', blank=False, null=False)
    package_old_price = models.IntegerField(blank=True, null=True)
    package_new_price = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return str(self.tour_place)


    def get_package_url(self):
        return reverse('package_app:package_details', kwargs={'slug': self.slug})