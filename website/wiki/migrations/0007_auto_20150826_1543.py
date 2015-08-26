# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wiki.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_auto_20150826_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('background', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('navigation', wagtail.wagtailcore.blocks.ListBlock(wiki.models.WikiPageLink, template='wiki/blocks/wiki_page_list.html')), ('page_feed', wagtail.wagtailcore.blocks.PageChooserBlock(template='wiki/blocks/wiki_page_feed.html')))),
        ),
    ]
