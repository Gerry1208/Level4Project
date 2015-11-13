# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0004_auto_20151113_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpicture',
            name='file',
            field=models.ImageField(null=True, upload_to=b'card_images'),
        ),
    ]
