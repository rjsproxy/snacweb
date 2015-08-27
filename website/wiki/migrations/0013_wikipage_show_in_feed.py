# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0012_auto_20150827_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipage',
            name='show_in_feed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
