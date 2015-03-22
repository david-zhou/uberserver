# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0010_auto_20150317_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_ride',
            name='final_fee',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
