# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0007_auto_20150902_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('container', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text', template='wiki/blocks/rich_text.html')), ('news_feed', wagtail.wagtailcore.blocks.PageChooserBlock(label='News Feed', template='wiki/blocks/news_feed.html'))), template='wiki/blocks/container.html')),)),
        ),
    ]
