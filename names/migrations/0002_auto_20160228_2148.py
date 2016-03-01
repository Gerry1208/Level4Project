# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='group_name',
            field=models.CharField(max_length=40, unique=True, serialize=False, primary_key=True),
        ),
    ]
