# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseID', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('latlon', models.CharField(max_length=50)),
                ('MtoTprice', models.CharField(max_length=50)),
                ('FtoSprice', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('DrivingRange', models.BooleanField(default=False)),
                ('Public', models.BooleanField(default=False)),
                ('Private', models.BooleanField(default=False)),
                ('Lessons', models.BooleanField(default=False)),
                ('ClubRental', models.BooleanField(default=False)),
                ('PuttingGreen', models.BooleanField(default=False)),
                ('LockerRoom', models.BooleanField(default=False)),
                ('CaddieHire', models.BooleanField(default=False)),
                ('ProShop', models.BooleanField(default=False)),
                ('Restaurant', models.BooleanField(default=False)),
                ('WaterHazards', models.BooleanField(default=False)),
                ('Bunkers', models.BooleanField(default=False)),
                ('ParThree', models.BooleanField(default=False)),
                ('MiniGolf', models.BooleanField(default=False)),
                ('NineHolePlay', models.BooleanField(default=False)),
                ('EighteenHolePlay', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
            bases=(models.Model,),
        ),
    ]
