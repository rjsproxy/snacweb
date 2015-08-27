# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0013_wikipage_show_in_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikipage',
            name='show_in_feed',
        ),
    ]
