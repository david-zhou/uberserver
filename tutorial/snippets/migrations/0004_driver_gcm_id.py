# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20150303_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='gcm_id',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
