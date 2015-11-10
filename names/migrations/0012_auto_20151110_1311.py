# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0011_auto_20151110_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pictures',
            name='group_id',
        ),
        migrations.DeleteModel(
            name='pictures',
        ),
        migrations.AddField(
            model_name='card',
            name='file',
            field=models.FileField(null=True, upload_to=b'/static/images'),
            preserve_default=True,
        ),
    ]
