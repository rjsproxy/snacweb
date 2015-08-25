# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='wiki.WikiPage')),
                ('tag', models.ForeignKey(related_name='wiki_wikipagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='wikipagetags',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='wikipagetags',
            name='tag',
        ),
        migrations.DeleteModel(
            name='WikiPageTags',
        ),
        migrations.AddField(
            model_name='wikipage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='wiki.WikiPageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
