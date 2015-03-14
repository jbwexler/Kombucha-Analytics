# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KA_app', '0002_auto_20150312_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bottle',
            old_name='type',
            new_name='bottleType',
        ),
        migrations.AddField(
            model_name='bottle',
            name='air',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='flavor',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'ginger', b'ginger'), (b'lemon', b'lemon')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='avgRating',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='joeRating',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bottle',
            name='tyRating',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
