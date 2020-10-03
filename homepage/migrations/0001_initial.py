# Generated by Django 3.1.1 on 2020-09-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('posted_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['-posted_at'],
            },
        ),
        migrations.CreateModel(
            name='roast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('posted_at', models.DateTimeField()),
            ],
            options={
                'ordering': ['-posted_at'],
            },
        ),
    ]
