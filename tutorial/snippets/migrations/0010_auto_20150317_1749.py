# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_auto_20150317_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_ride',
            name='final_lat',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='final_long',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='initial_lat',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_ride',
            name='initial_long',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
