# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0005_auto_20151113_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='group_name',
            field=models.CharField(max_length=10, unique=True, serialize=False, primary_key=True),
        ),
    ]
