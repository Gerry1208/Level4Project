# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0010_auto_20151116_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='bulkUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'csv_files')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
