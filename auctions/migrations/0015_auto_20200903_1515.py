# Generated by Django 3.1 on 2020-09-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_bid_isopen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='isOpen',
        ),
        migrations.AddField(
            model_name='listing',
            name='isOpen',
            field=models.BooleanField(default=True),
        ),
    ]
