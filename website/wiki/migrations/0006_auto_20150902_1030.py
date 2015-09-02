# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_auto_20150902_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text')), ('news_feed', wagtail.wagtailcore.blocks.StructBlock((('root_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Root Page')),), label='News Feed')))),
        ),
    ]
