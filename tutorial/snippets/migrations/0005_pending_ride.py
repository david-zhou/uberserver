# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_driver_gcm_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pending_Ride',
            fields=[
                ('pending_ride_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_lat', models.FloatField()),
                ('user_lon', models.FloatField()),
                ('user_id', models.ForeignKey(to='snippets.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
