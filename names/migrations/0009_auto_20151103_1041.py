# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0008_auto_20151103_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmodel',
            old_name='username',
            new_name='user',
        ),
    ]
