# Generated by Django 5.0 on 2023-12-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='photo_video',
            field=models.FileField(blank=True, upload_to='shops_photo/'),
        ),
    ]
