# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('label', models.CharField(help_text='The label of the form field', verbose_name='Label', max_length=255)),
                ('field_type', models.CharField(verbose_name='Field type', max_length=16, choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')])),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', blank=True, verbose_name='Choices', max_length=512)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', blank=True, verbose_name='Default value', max_length=255)),
                ('help_text', models.CharField(blank=True, verbose_name='Help text', max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True)),
                ('to_address', models.CharField(help_text='Optional - form submissions will be emailed to this address', blank=True, verbose_name='To address', max_length=255)),
                ('from_address', models.CharField(blank=True, verbose_name='From address', max_length=255)),
                ('subject', models.CharField(blank=True, verbose_name='Subject', max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='form_fields', to='form.FormPage'),
        ),
    ]
