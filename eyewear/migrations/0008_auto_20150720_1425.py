# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0007_glasses_frame_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(to='eyewear.Item'),
        ),
        migrations.AlterField(
            model_name='glasses',
            name='frame_name',
            field=models.TextField(),
        ),
    ]
