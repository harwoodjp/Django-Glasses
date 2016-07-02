# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyewear', '0005_auto_20150713_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glasses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(related_name='cart_items', to='eyewear.Cart2'),
        ),
    ]
