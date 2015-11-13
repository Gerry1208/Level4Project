# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0002_auto_20151113_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpicture',
            name='file',
            field=models.ImageField(null=True, upload_to=b'static/images'),
        ),
    ]
