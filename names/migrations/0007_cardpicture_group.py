# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0006_auto_20151114_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpicture',
            name='group',
            field=models.ForeignKey(default='a', to='names.groupModel'),
            preserve_default=False,
        ),
    ]
