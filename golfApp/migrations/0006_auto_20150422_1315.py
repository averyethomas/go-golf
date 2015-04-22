# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfApp', '0005_auto_20150420_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='latlon',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
