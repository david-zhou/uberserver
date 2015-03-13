# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_user_ride_pending_ride_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='license_plate',
            field=models.CharField(blank=True, max_length=10),
            preserve_default=True,
        ),
    ]
