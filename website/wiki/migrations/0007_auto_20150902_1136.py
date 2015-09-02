# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wiki', '0006_auto_20150902_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipage',
            name='blurb',
            field=models.TextField(default='', help_text='Short description of the page.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikipage',
            name='icon',
            field=models.ForeignKey(blank=True, to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, related_name='+', null=True),
        ),
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text')), ('news_feed', wagtail.wagtailcore.blocks.StructBlock((('root_page', wagtail.wagtailcore.blocks.PageChooserBlock(label='Root Page')),), label='News Feed', template='wiki/blocks/news_feed.html')))),
        ),
    ]
