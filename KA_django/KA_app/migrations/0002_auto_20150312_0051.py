# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KA_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('teaStrength', models.IntegerField()),
                ('sugarConc', models.FloatField()),
                ('waterVol', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('volume', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scoby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ManyToManyField(related_name='parent_rel_+', to='KA_app.Scoby')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.ManyToManyField(related_name='teas', to='KA_app.Enum')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='container',
            name='shape',
            field=models.ManyToManyField(related_name='containers', to='KA_app.Enum'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='container',
            field=models.ManyToManyField(related_name='brews', to='KA_app.Container'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='sugarType',
            field=models.ManyToManyField(related_name='brews_sugar', to='KA_app.Enum'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='teaType',
            field=models.ManyToManyField(related_name='brews', to='KA_app.Tea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='waterType',
            field=models.ManyToManyField(related_name='brews_water', to='KA_app.Enum'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='brew',
            field=models.ManyToManyField(related_name='names', to='KA_app.Brew'),
            preserve_default=True,
        ),
    ]
