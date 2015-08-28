# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0016_auto_20150828_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('thumbnail', wagtail.wagtailcore.blocks.StreamBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title for thumnail.')), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False, help_text='Thumbnail description shown if space permits.')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Image to show in thumbnail.'))))), ('page', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title for thumnail.')), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False, help_text='Thumbnail description shown if space permits.')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Image to show in thumbnail.')), ('page', wagtail.wagtailcore.blocks.PageChooserBlock()))))))))),
        ),
    ]
