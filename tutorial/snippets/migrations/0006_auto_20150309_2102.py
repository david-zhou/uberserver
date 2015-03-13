# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_pending_ride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_ride',
            name='date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='distance',
            field=models.DecimalField(null=True, decimal_places=1, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='driver_rating',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='fee',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='user_rating',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
