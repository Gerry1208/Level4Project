# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0009_auto_20151103_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='picture',
        ),
        migrations.AddField(
            model_name='card',
            name='file',
            field=models.FileField(null=True, upload_to=b'/static/images'),
            preserve_default=True,
        ),
    ]
