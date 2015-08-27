# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wiki', '0011_auto_20150827_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True, to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='blank', max_length=64),
            preserve_default=False,
        ),
    ]
