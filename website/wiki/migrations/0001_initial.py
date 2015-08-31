# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='wagtailcore.Page', primary_key=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()),))),
                ('show_in_feed', models.BooleanField(default=False, help_text='Include page in site feeds: e.g., front page.')),
            ],
            options={
                'abstract': False,
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
            field=modelcluster.contrib.taggit.ClusterTaggableManager(through='wiki.WikiPageTag', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True),
        ),
    ]
