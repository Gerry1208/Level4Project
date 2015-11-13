# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0003_auto_20151113_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpicture',
            name='student',
            field=models.ForeignKey(to='names.card'),
        ),
    ]
