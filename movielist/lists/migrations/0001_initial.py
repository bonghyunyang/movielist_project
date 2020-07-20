# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-07-20 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('genres', models.CharField(max_length=50)),
                ('summary', models.TextField()),
            ],
        ),
    ]