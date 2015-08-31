# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikipage',
            name='show_in_feed',
        ),
        migrations.AddField(
            model_name='wikipage',
            name='show_in_news',
            field=models.BooleanField(default=False, help_text='Include page in site news: e.g., front page.'),
        ),
    ]
