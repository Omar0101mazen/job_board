# Generated by Django 4.0.5 on 2022-11-20 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply_titl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='title',
            new_name='job',
        ),
    ]
