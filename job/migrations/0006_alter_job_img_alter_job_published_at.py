# Generated by Django 4.0.5 on 2022-10-28 19:24

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(upload_to=job.models.photo),
        ),
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
