# Generated by Django 4.0 on 2021-12-17 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_emplo_delete_employee_alter_movie_release_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 17, 6, 24, 33, 333057)),
        ),
    ]