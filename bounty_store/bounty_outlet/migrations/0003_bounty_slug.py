# Generated by Django 3.2.9 on 2021-11-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty_outlet', '0002_auto_20211124_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
