# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailembeds.blocks
import wagtail.wagtailcore.fields
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import modelcluster.fields
import wagtail.wagtailimages.blocks
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailimages', '0008_image_created_at_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('blurb', models.TextField(help_text='Short description of the page.')),
                ('content', wagtail.wagtailcore.fields.StreamField((('container', wagtail.wagtailcore.blocks.StreamBlock((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(label='Rich Text')), ('news_feed', wagtail.wagtailcore.blocks.PageChooserBlock(template='wiki/blocks/news_feed.html', label='News Feed')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(label='Embed')), ('image', wagtail.wagtailcore.blocks.StructBlock((('align', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('pull-left', 'Pull Left'), ('pull-right', 'Pull Right'), ('center-block', 'Center Block')], required=False)), ('shape', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('img-rounded', 'Rounded'), ('img-circle', 'Circle'), ('img-thumbnail', 'Thumbnail')], required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), label='Image'))))),))),
                ('show_in_news', models.BooleanField(default=False, help_text='Include page in site news: e.g., front page.')),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Wiki Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WikiPageTag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(to='wiki.WikiPage', related_name='tagged_items')),
                ('tag', models.ForeignKey(to='taggit.Tag', related_name='wiki_wikipagetag_items')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='wikipage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', through='wiki.WikiPageTag', verbose_name='Tags', blank=True),
        ),
    ]
