# Generated by Django 3.1 on 2020-08-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200829_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='isWatchlisted',
            field=models.BooleanField(default=False),
        ),
    ]