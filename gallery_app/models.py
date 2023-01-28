from django.db import models
from django.urls import reverse
# Create your models here.

class Gallery(models.Model):
    place_name = models.CharField(max_length=255)
    place_description = models.CharField(max_length=255)
    place_image = models.ImageField(upload_to='place_images')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.place_name)


    def get_gallery_url(self):
        return reverse('gallery_app:gallery_details', kwargs={'slug': self.slug})


class GalleryImages(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.FileField(upload_to='place_gallery')

    def __str__(self):
        return str(self.gallery.place_name)