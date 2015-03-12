# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150312_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottle',
            name='brew',
            field=models.ManyToManyField(related_name='names', null=True, to='polls.Brew', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='endDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='startDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='container',
            field=models.ManyToManyField(related_name='brews', null=True, to='polls.Container', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='endDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='sugarConc',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='sugarType',
            field=models.ManyToManyField(related_name='brews_sugar', null=True, to='polls.Enum', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='teaStrength',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='teaType',
            field=models.ManyToManyField(related_name='brews', null=True, to='polls.Tea', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='waterType',
            field=models.ManyToManyField(related_name='brews_water', null=True, to='polls.Enum', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brew',
            name='waterVol',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='container',
            name='shape',
            field=models.ManyToManyField(related_name='containers', null=True, to='polls.Enum', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='container',
            name='volume',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scoby',
            name='parent',
            field=models.ManyToManyField(related_name='parent_rel_+', null=True, to='polls.Scoby', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tea',
            name='type',
            field=models.ManyToManyField(related_name='teas', null=True, to='polls.Enum', blank=True),
            preserve_default=True,
        ),
    ]
