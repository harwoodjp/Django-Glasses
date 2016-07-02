# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0006_auto_20150720_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='glasses',
            name='frame_name',
            field=models.CharField(max_length=200, default='NULL'),
        ),
    ]
