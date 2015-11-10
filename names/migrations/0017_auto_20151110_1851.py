# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0016_auto_20151110_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardpicture',
            old_name='student_id',
            new_name='student',
        ),
    ]
