# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshaper', '0004_auto_20150531_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
