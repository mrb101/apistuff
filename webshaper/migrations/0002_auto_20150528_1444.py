# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshaper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billto',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(to='webshaper.Customer'),
        ),
        migrations.AlterField(
            model_name='modifier',
            name='product',
            field=models.ForeignKey(to='webshaper.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(to='webshaper.Customer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='webshaper.Category'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='modifier',
            field=models.ForeignKey(to='webshaper.Modifier'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(to='webshaper.Product'),
        ),
    ]
