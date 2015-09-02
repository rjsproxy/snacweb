# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20150902_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text')), ('page_feed', wagtail.wagtailcore.blocks.StructBlock((('root_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Root Page')),), label='Page Feed')))),
        ),
    ]
