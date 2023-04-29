from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    flag_image = models.ImageField(upload_to='flag_images')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return str(self.name)
    


class Visa(models.Model):
    where_from = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='where_from', verbose_name="Where am I From?")
    where_going = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='where_going', verbose_name="Where am I Going?")
    type_name = (
        (1, "Business"),
        (2, "Tourist"),
        (3, "Medical"),
        (3, "Student"),
    )
    visa_type = models.IntegerField(choices=type_name)
    which_country_passport = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='which_country_passport')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=100)
    nid_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="NID Number")
    occupation_name = (
        (1, "Student"),
        (2, "Government Job"),
        (3, "Private Job"),
        (4, "Business"),
        (5, "Teacher"),
        (6, "Doctor"),
        (7, "Other"),
    )
    occupation = models.IntegerField(choices=occupation_name)
    gender_name = (
        (1, "Male"),
        (2, "Female"),
    )
    gender = models.IntegerField(choices=gender_name)
    date_of_birth = models.DateField()

    def __str__(self):
        return str(self.name)
    


class Popular_Destination(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    feature_image = models.ImageField(upload_to='flag_images')
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return str(self.name)





class Flight(models.Model):
    flight_type = models.CharField(max_length=250)
    flying_from = models.CharField(max_length=250)
    flying_to = models.CharField(max_length=250)
    departing = models.CharField(max_length=250)
    returning = models.CharField(max_length=250)
    adults = models.CharField(max_length=250)
    children = models.CharField(max_length=250)
    travel_class =models.CharField(max_length=250)


    def __str__(self):
        return str(self.flight_type)
    


class Passport(models.Model):
    full_name = models.CharField(max_length=50)
    gender_name = (
        (1, "Male"),
        (2, "Female"),
    )
    gender = models.IntegerField(choices=gender_name)
    date_of_birth = models.DateField()
    birth_certificate = models.CharField(max_length=50)
    nid_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="NID Number")
    occupation_name = (
        (1, "Student"),
        (2, "Government Job"),
        (3, "Private Job"),
        (4, "Business"),
        (5, "Teacher"),
        (6, "Doctor"),
        (7, "Other"),
    )
    occupation = models.IntegerField(choices=occupation_name)
    father_name = models.CharField(max_length=50)
    father_nid = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    mother_nid = models.CharField(max_length=50)
    present_address = models.TextField()
    permanent_address = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return str(self.full_name)
    



