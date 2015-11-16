# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0007_cardpicture_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardpicture',
            name='group',
        ),
    ]
