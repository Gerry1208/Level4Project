# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0004_auto_20151024_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='picture',
            field=models.FileField(upload_to=b'card_images/%groups.user/%groups.group_name', blank=True),
        ),
    ]
