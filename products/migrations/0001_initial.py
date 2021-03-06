# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField(default='', max_length=300)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
