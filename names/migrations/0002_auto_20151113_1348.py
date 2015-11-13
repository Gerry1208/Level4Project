# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpicture',
            name='student',
            field=models.OneToOneField(to='names.card'),
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='group_name',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
