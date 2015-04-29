# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfApp', '0008_course_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Image', blank=True),
            preserve_default=True,
        ),
    ]
