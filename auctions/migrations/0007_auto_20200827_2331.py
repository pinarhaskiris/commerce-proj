# Generated by Django 3.1 on 2020-08-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='creationDate',
            field=models.DateField(),
        ),
    ]
