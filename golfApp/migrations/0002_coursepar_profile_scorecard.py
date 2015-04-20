# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('golfApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursePar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hole1', models.IntegerField(null=True, blank=True)),
                ('hole2', models.IntegerField(null=True, blank=True)),
                ('hole3', models.IntegerField(null=True, blank=True)),
                ('hole4', models.IntegerField(null=True, blank=True)),
                ('hole5', models.IntegerField(null=True, blank=True)),
                ('hole6', models.IntegerField(null=True, blank=True)),
                ('hole7', models.IntegerField(null=True, blank=True)),
                ('hole8', models.IntegerField(null=True, blank=True)),
                ('hole9', models.IntegerField(null=True, blank=True)),
                ('hole10', models.IntegerField(null=True, blank=True)),
                ('hole11', models.IntegerField(null=True, blank=True)),
                ('hole12', models.IntegerField(null=True, blank=True)),
                ('hole13', models.IntegerField(null=True, blank=True)),
                ('hole14', models.IntegerField(null=True, blank=True)),
                ('hole15', models.IntegerField(null=True, blank=True)),
                ('hole16', models.IntegerField(null=True, blank=True)),
                ('hole17', models.IntegerField(null=True, blank=True)),
                ('hole18', models.IntegerField(null=True, blank=True)),
                ('course', models.OneToOneField(to='golfApp.Course')),
            ],
            options={
                'verbose_name_plural': 'coursePars',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'', null=True, verbose_name=b'photos', blank=True)),
                ('hometown', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('birthdate', models.DateField(null=True, blank=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scorecard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userHole1', models.IntegerField(null=True, blank=True)),
                ('userHole2', models.IntegerField(null=True, blank=True)),
                ('userHole3', models.IntegerField(null=True, blank=True)),
                ('userHole4', models.IntegerField(null=True, blank=True)),
                ('userHole5', models.IntegerField(null=True, blank=True)),
                ('userHole6', models.IntegerField(null=True, blank=True)),
                ('userHole7', models.IntegerField(null=True, blank=True)),
                ('userHole8', models.IntegerField(null=True, blank=True)),
                ('userHole9', models.IntegerField(null=True, blank=True)),
                ('userHole10', models.IntegerField(null=True, blank=True)),
                ('userHole11', models.IntegerField(null=True, blank=True)),
                ('userHole12', models.IntegerField(null=True, blank=True)),
                ('userHole13', models.IntegerField(null=True, blank=True)),
                ('userHole14', models.IntegerField(null=True, blank=True)),
                ('userHole15', models.IntegerField(null=True, blank=True)),
                ('userHole16', models.IntegerField(null=True, blank=True)),
                ('userHole17', models.IntegerField(null=True, blank=True)),
                ('userHole18', models.IntegerField(null=True, blank=True)),
                ('course', models.ForeignKey(to='golfApp.Course')),
                ('coursePar', models.ForeignKey(to='golfApp.coursePar')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Scorecards',
            },
            bases=(models.Model,),
        ),
    ]
