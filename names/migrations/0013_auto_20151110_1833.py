# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0012_auto_20151110_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(null=True, upload_to=b'/static/images')),
                ('student_id', models.ForeignKey(to='names.card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='card',
            name='file',
        ),
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.CharField(max_length=9, serialize=False, primary_key=True),
        ),
    ]
