# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_driver_license_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_ride',
            name='user_destination_lat',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pending_ride',
            name='user_destination_lon',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pending_ride',
            name='user_lat',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pending_ride',
            name='user_lon',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
