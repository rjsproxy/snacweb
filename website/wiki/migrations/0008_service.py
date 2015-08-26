# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wiki', '0007_auto_20150826_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=64)),
                ('link', models.URLField(null=True, blank=True)),
                ('icon', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, to='wagtailimages.Image')),
            ],
        ),
    ]
