# Generated by Django 3.1 on 2020-08-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200829_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='startingBid',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='listing',
            name='imgUrl',
            field=models.CharField(max_length=512),
        ),
    ]
