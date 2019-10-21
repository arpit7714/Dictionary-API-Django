# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-27 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20180325_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_number', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('new_driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NewDriver', to='users.InoDriver')),
                ('previous_driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreviousDriver', to='users.InoDriver')),
            ],
        ),
    ]