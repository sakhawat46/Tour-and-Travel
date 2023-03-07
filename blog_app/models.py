from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=255, verbose_name='Put a Title')
    short_description = models.TextField(max_length=500)
    blog_content = RichTextField()
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image', blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return str(self.blog_title)