# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('label', models.CharField(help_text='The label of the form field', verbose_name='Label', max_length=255)),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], verbose_name='Field type', max_length=16)),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='Choices', max_length=512, blank=True)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', verbose_name='Default value', max_length=255, blank=True)),
                ('help_text', models.CharField(verbose_name='Help text', max_length=255, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('to_address', models.CharField(help_text='Optional - form submissions will be emailed to this address', verbose_name='To address', max_length=255, blank=True)),
                ('from_address', models.CharField(verbose_name='From address', max_length=255, blank=True)),
                ('subject', models.CharField(verbose_name='Subject', max_length=255, blank=True)),
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
            field=modelcluster.fields.ParentalKey(to='form.FormPage', related_name='form_fields'),
        ),
    ]
