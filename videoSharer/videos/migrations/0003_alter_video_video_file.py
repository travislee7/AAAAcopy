# Generated by Django 4.1.7 on 2023-08-09 02:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='uploads/video_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov'])]),
        ),
    ]
