# Generated by Django 4.0.5 on 2023-02-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_imag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='imag',
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]