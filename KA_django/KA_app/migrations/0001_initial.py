# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('startDate', models.DateField(null=True, blank=True)),
                ('endDate', models.DateField(null=True, blank=True)),
                ('volume', models.FloatField(null=True, blank=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True, choices=[(b'beer', b'beer'), (b"gt's", b"gt's")])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField(null=True, blank=True)),
                ('endDate', models.DateField(null=True, blank=True)),
                ('brewTime', models.IntegerField(null=True, blank=True)),
                ('teaStrength', models.IntegerField(null=True, blank=True)),
                ('waterType', models.CharField(blank=True, max_length=200, null=True, choices=[(b'filtered', b'filtered'), (b'unfiltered', b'unfiltered')])),
                ('waterVol', models.FloatField(null=True, blank=True)),
                ('sugarType', models.CharField(blank=True, max_length=200, null=True, choices=[(b'white', b'white'), (b'brown', b'brown'), (b'honey', b'honey'), (b'local honey', b'local honey')])),
                ('sugarConc', models.FloatField(null=True, blank=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True, choices=[(b'Tyler', b'Tyler'), (b'Joe', b'Joe')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('volume', models.FloatField(null=True, blank=True)),
                ('shape', models.CharField(blank=True, max_length=200, null=True, choices=[(b'tall', b'tall'), (b'wide', b'wide')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scoby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('dateCreated', models.DateField(null=True, blank=True)),
                ('parent', models.ManyToManyField(related_name='parent_rel_+', null=True, to='KA_app.Scoby', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True, choices=[(b'green', b'green'), (b'white', b'white'), (b'oolong', b'oolong'), (b'shou', b'shou'), (b'sheng', b'sheng')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='brew',
            name='container',
            field=models.ManyToManyField(related_name='brews', null=True, to='KA_app.Container', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='scoby',
            field=models.ManyToManyField(related_name='brews', null=True, to='KA_app.Scoby', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='teaType',
            field=models.ManyToManyField(related_name='brews', null=True, to='KA_app.Tea', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='brew',
            field=models.ManyToManyField(related_name='bottles', null=True, to='KA_app.Brew', blank=True),
            preserve_default=True,
        ),
    ]
