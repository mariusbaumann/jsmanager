# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cVideofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('videoTitle', models.CharField(max_length=200)),
                ('timeCreated', models.DateTimeField(verbose_name=b'date published')),
                ('length', models.IntegerField(default=0)),
                ('frames', models.IntegerField(default=0)),
                ('framesDone', models.IntegerField(default=0)),
                ('codingString', models.CharField(max_length=500)),
            ],
        ),
    ]
