from django.db import models

# Create your models here.


class Home(models.Model):
    video_title = models.CharField(max_length=50)
    video_short_description = models.CharField(max_length=255)
    video_uplode = models.FileField(upload_to='videos_uploaded')

    def __str__(self):
        return str(self.video_title)