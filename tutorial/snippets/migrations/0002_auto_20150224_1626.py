# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_Card',
            fields=[
                ('credit_card_number', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('mm', models.CharField(max_length=2)),
                ('yy', models.CharField(max_length=2)),
                ('cvv', models.CharField(max_length=3)),
                ('postal_code', models.CharField(blank=True, max_length=5)),
                ('mail', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('vehicle', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('pos_lat', models.CharField(blank=True, max_length=20)),
                ('pos_long', models.CharField(blank=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(primary_key=True, max_length=50, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('home', models.CharField(blank=True, max_length=50)),
                ('home_lat', models.CharField(blank=True, max_length=20)),
                ('home_long', models.CharField(blank=True, max_length=20)),
                ('work', models.CharField(blank=True, max_length=50)),
                ('work_lat', models.CharField(blank=True, max_length=20)),
                ('work_long', models.CharField(blank=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Ride',
            fields=[
                ('ride_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True)),
                ('initial_pos', models.CharField(blank=True, max_length=50)),
                ('initial_lat', models.CharField(blank=True, max_length=20)),
                ('initial_long', models.CharField(blank=True, max_length=20)),
                ('final_pos', models.CharField(blank=True, max_length=50)),
                ('final_lat', models.CharField(blank=True, max_length=20)),
                ('final_long', models.CharField(blank=True, max_length=20)),
                ('distance', models.DecimalField(blank=True, max_digits=5, decimal_places=1)),
                ('time', models.CharField(blank=True, max_length=10)),
                ('fee', models.IntegerField(blank=True)),
                ('user_rating', models.IntegerField(blank=True)),
                ('driver_rating', models.IntegerField(blank=True)),
                ('credit_card_number', models.ForeignKey(to='snippets.Credit_Card')),
                ('driver_id', models.ForeignKey(to='snippets.Driver')),
                ('user_id', models.ForeignKey(to='snippets.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='credit_card',
            name='email',
            field=models.ForeignKey(to='snippets.User'),
            preserve_default=True,
        ),
    ]
