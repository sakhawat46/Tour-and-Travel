# Generated by Django 3.1 on 2023-04-29 08:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0004_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular_Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('feature_image', models.ImageField(upload_to='flag_images')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
