# Generated by Django 3.1.1 on 2020-10-02 23:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boast',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 23, 51, 52, 751304)),
        ),
    ]
