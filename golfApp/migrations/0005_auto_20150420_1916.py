# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfApp', '0004_auto_20150420_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseID',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='coursePar',
        ),
    ]
