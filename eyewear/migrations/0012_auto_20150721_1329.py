# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0011_auto_20150721_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='glasses',
            name='brand',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='glasses',
            name='frame_color_type',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='glasses',
            name='gender_type',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='glasses',
            name='material_type',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='glasses',
            name='product_group_type',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(to='eyewear.Item'),
        ),
    ]
