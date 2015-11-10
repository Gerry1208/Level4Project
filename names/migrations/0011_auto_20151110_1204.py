# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0010_auto_20151110_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='pictures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(default=b'C:\\Users\\Gerry\\Downloads\\d4zWOgz.jpg', upload_to=b'/static/images')),
                ('group_id', models.ForeignKey(to='names.groupModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='card',
            name='file',
        ),
    ]
