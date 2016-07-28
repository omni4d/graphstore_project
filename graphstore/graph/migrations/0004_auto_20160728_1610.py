# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 16:10
from __future__ import unicode_literals

from django.db import migrations


def create_edgetypes(apps, schema_editor):
    EdgeType = apps.get_model('graph', 'EdgeType')
    for edgetype in ['part', 'subpart', 'class', 'member']:
        EdgeType(name=edgetype).save()


def delete_edgetypes(apps, schema_editor):
    EdgeType = apps.get_model('graph', 'EdgeType')
    EdgeType.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_edgetype'),
    ]

    operations = [
        migrations.RunPython(create_edgetypes, delete_edgetypes)
    ]
