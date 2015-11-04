# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0006_auto_20151102_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='group.html',
            new_name='group',
        ),
    ]
