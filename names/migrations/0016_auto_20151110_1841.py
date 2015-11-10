# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0015_auto_20151110_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='studentid',
            new_name='student',
        ),
    ]
