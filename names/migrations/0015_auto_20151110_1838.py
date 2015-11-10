# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0014_auto_20151110_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='student_id',
            new_name='studentid',
        ),
    ]
