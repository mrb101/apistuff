# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('addressline1', models.CharField(max_length=200)),
                ('addressline2', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('extra', models.CharField(max_length=100)),
                ('customer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=30)),
                ('status', models.CharField(default=b'Draft', max_length=20, choices=[(b'Live', b'Live'), (b'Draft', b'Draft')])),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('product', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True, max_length=30)),
                ('Title', models.CharField(max_length=30)),
                ('parent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('product', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.IntegerField()),
                ('orderstatus', models.CharField(default=b'', max_length=20, choices=[(b'Incomplete', b'Order is Incomplete'), (b'Pending', b'Order is Pending'), (b'Processed', b'Order is Processed'), (b'Shipped', b'Order is Shipped'), (b'Canceled', b'Order is Canceled')])),
                ('subtotal', models.DecimalField(max_digits=5, decimal_places=2)),
                ('shippingprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('total', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('product', models.IntegerField()),
                ('sku', models.CharField(unique=True, max_length=30)),
                ('quantity', models.IntegerField()),
                ('taxrate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('taxband', models.DecimalField(max_digits=5, decimal_places=2)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(unique=True, max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, max_length=30)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('saleprice', models.DecimalField(null=True, max_digits=5, decimal_places=2)),
                ('productstatus', models.CharField(default=b'Draft', max_length=10, choices=[(b'Live', b'Live'), (b'Draft', b'DRAFT')])),
                ('stockstatus', models.CharField(default=b'In Stock', max_length=30, choices=[(b'In Stock', b'In Stock'), (b'Running Out', b'Running Out'), (b'Out of Stock', b'No Stock'), (b'Discontinued', b'Discontinued'), (b'Ordered', b'Ordered')])),
                ('stocklevel', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('shipping', models.BooleanField(default=True)),
                ('weight', models.DecimalField(max_digits=5, decimal_places=5)),
                ('height', models.DecimalField(max_digits=5, decimal_places=5)),
                ('width', models.DecimalField(max_digits=5, decimal_places=5)),
                ('depth', models.DecimalField(max_digits=5, decimal_places=5)),
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('pricemod', models.DecimalField(max_digits=5, decimal_places=2)),
                ('modifier', models.IntegerField()),
                ('product', models.IntegerField()),
            ],
        ),
    ]
