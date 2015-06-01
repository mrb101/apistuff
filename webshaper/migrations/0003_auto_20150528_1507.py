# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webshaper', '0002_auto_20150528_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 4, 27, 17172), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 4, 49, 888517), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 5, 2, 376658), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 5, 17, 857869), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 5, 27, 161512), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 5, 36, 273344), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 5, 44, 137403), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 5, 52, 944906), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modifier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 1, 952664), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modifier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 10, 304537), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 17, 385032), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 25, 856546), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 34, 208326), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 41, 416042), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 48, 952389), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 6, 55, 48138), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 7, 4, 847800), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variation',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 15, 7, 12, 399869), auto_now=True),
            preserve_default=False,
        ),
    ]
