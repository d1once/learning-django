# Generated by Django 3.2.9 on 2021-12-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty_outlet', '0005_auto_20211201_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.AddField(
            model_name='bounty',
            name='published_countries',
            field=models.ManyToManyField(to='bounty_outlet.State'),
        ),
    ]
