# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KA_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottle',
            name='avgRating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='bottleTime',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='joeRating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bottle',
            name='tyRating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
