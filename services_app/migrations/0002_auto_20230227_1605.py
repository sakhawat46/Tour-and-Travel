# Generated by Django 3.1 on 2023-02-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='visa_type',
            field=models.IntegerField(choices=[(1, 'Business'), (2, 'Tourist'), (3, 'Medical'), (3, 'Student')]),
        ),
    ]
