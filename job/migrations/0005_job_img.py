# Generated by Django 4.0.5 on 2022-10-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='img',
            field=models.ImageField(default='', upload_to='img/'),
            preserve_default=False,
        ),
    ]
