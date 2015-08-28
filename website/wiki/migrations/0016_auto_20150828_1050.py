# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wiki.models
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0015_wikipage_show_in_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('thumbnails', wagtail.wagtailcore.blocks.ListBlock(wiki.models.ThumbBlock, template='wiki/blocks/thumbnails.html')))),
        ),
    ]
