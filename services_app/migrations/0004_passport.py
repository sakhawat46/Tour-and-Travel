# Generated by Django 3.1 on 2023-04-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0003_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('date_of_birth', models.DateField()),
                ('birth_certificate', models.CharField(max_length=50)),
                ('nid_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='NID Number')),
                ('occupation', models.IntegerField(choices=[(1, 'Student'), (2, 'Government Job'), (3, 'Private Job'), (4, 'Business'), (5, 'Teacher'), (6, 'Doctor'), (7, 'Other')])),
                ('father_name', models.CharField(max_length=50)),
                ('father_nid', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('mother_nid', models.CharField(max_length=50)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
