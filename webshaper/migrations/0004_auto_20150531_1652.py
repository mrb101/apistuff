# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshaper', '0003_auto_20150528_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Title',
            new_name='title',
        ),
    ]
