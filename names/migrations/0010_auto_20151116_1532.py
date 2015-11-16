# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0009_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='group',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
