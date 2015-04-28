# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfApp', '0006_auto_20150422_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='phone',
        ),
        migrations.AddField(
            model_name='course',
            name='architect',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='backPar',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='backSlope',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='backTees',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='courseType',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='FtoSprice',
            field=models.CharField(max_length=50, verbose_name=b'Weekend Price'),
        ),
        migrations.AlterField(
            model_name='course',
            name='MtoTprice',
            field=models.CharField(max_length=50, verbose_name=b'Weekday Price'),
        ),
        migrations.AlterField(
            model_name='course',
            name='latlon',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Geocoordinates', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='site',
            field=models.CharField(max_length=50, verbose_name=b'Website'),
        ),
    ]
