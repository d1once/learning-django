# Generated by Django 3.2.9 on 2021-11-24 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='benefactor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='deadoralive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='reward',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
