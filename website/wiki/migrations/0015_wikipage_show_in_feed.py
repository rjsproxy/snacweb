# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_remove_wikipage_show_in_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipage',
            name='show_in_feed',
            field=models.BooleanField(help_text='Include page in site feeds: e.g., front page.', default=False),
        ),
    ]
