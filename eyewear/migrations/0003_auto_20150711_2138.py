# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
