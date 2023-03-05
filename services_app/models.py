from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

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