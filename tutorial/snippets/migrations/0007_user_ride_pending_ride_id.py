# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20150309_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_ride',
            name='pending_ride_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
