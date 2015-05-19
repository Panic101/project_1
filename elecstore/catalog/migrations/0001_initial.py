# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory_name', models.CharField(max_length=200)),
                ('total_items', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=200)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product_directory', models.ForeignKey(to='catalog.ProductDirectory')),
            ],
        ),
    ]
