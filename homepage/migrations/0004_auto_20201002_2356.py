# Generated by Django 3.1.1 on 2020-10-02 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20201002_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boast',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='roast',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
