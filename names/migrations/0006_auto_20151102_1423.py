# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0005_auto_20151028_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='picture',
            field=models.FileField(upload_to=b'/static/images', blank=True),
        ),
    ]
