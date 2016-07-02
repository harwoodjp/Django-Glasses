# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0010_auto_20150721_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glasses',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='glasses',
            name='frame_color_type',
        ),
        migrations.RemoveField(
            model_name='glasses',
            name='gender_type',
        ),
        migrations.RemoveField(
            model_name='glasses',
            name='material_type',
        ),
        migrations.RemoveField(
            model_name='glasses',
            name='product_group_type',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(to='eyewear.Item'),
        ),
    ]
