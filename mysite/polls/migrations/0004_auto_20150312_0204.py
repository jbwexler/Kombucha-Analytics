# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150312_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='bottleType',
            field=models.ManyToManyField(related_name='bottles_type', null=True, to='polls.Enum', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='shape',
            field=models.ManyToManyField(related_name='bottles_shape', null=True, to='polls.Enum', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='volume',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='scoby',
            field=models.ManyToManyField(related_name='brews', null=True, to='polls.Scoby', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='brew',
            field=models.ManyToManyField(related_name='bottles', null=True, to='polls.Brew', blank=True),
            preserve_default=True,
        ),
    ]
