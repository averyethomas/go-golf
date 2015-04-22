# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfApp', '0003_auto_20150420_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='city',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='course',
            name='state',
        ),
        migrations.RemoveField(
            model_name='course',
            name='street',
        ),
        migrations.RemoveField(
            model_name='course',
            name='zipcode',
        ),
    ]
