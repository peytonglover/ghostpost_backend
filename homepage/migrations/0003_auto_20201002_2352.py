# Generated by Django 3.1.1 on 2020-10-02 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20201002_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boast',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 23, 52, 14, 540996)),
        ),
        migrations.AlterField(
            model_name='roast',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 23, 52, 14, 541537)),
        ),
    ]