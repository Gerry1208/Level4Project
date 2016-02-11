# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='group',
            field=models.ManyToManyField(to=b'names.groupModel'),
        ),
        migrations.AlterField(
            model_name='cardpicture',
            name='file',
            field=models.FileField(null=True, upload_to=b'card_images'),
        ),
        migrations.AlterField(
            model_name='groupmodel',
            name='group_name',
            field=models.CharField(max_length=40, unique=True, serialize=False, primary_key=True),
        ),
    ]
