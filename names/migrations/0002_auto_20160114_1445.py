# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='group',
            field=models.ManyToManyField(to=b'names.groupModel'),
        ),
    ]
