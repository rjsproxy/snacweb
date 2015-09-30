# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailembeds.blocks
import wiki.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('container', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text')), ('news_feed', wagtail.wagtailcore.blocks.PageChooserBlock(label='News Feed', template='wiki/blocks/news_feed.html')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(label='Embed')), ('image', wagtail.wagtailcore.blocks.StructBlock((('align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('pull-left', 'Pull Left'), ('pull-right', 'Pull Right'), ('center-block', 'Center Block')], required=False)), ('shape', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('img-rounded', 'Rounded'), ('img-circle', 'Circle'), ('img-thumbnail', 'Thumbnail')], required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), label='Image')), ('markdown', wiki.blocks.MarkDownBlock())))),)),
        ),
    ]
