# Generated by Django 5.0.8 on 2024-08-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog-images/'),
        ),
    ]
