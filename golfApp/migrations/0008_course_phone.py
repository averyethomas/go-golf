# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfApp', '0007_auto_20150428_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='phone',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
