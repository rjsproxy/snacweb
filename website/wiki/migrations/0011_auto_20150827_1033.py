# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailsnippets.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wiki.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wiki', '0010_auto_20150826_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='service',
            name='link',
        ),
        migrations.RemoveField(
            model_name='service',
            name='text',
        ),
        migrations.AddField(
            model_name='service',
            name='link_document',
            field=models.ForeignKey(related_name='+', to='wagtaildocs.Document', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='link_page',
            field=models.ForeignKey(related_name='+', to='wagtailcore.Page', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('service', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailsnippets.blocks.SnippetChooserBlock(wiki.models.Service), template='wiki/blocks/wiki_service_list.html')), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('navigation', wagtail.wagtailcore.blocks.ListBlock(wiki.models.WikiPageLink, template='wiki/blocks/wiki_page_list.html')), ('page_feed', wagtail.wagtailcore.blocks.PageChooserBlock(template='wiki/blocks/wiki_page_feed.html')))),
        ),
    ]
