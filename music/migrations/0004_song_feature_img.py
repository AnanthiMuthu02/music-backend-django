# Generated by Django 5.0.4 on 2024-04-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='feature_img',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
