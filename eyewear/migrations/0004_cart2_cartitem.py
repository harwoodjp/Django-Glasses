# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0003_auto_20150711_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart2',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(to='eyewear.Cart2', related_name='cart_items')),
                ('item', models.ForeignKey(to='eyewear.Item')),
            ],
        ),
    ]
