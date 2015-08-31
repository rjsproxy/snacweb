from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase

class WikiPageTag(TaggedItemBase):
    content_object = ParentalKey('wiki.WikiPage', related_name='tagged_items')

class WikiPage(Page):
    """
    Default content type for our site.  No one owns the page.  Anyone can edit
    it.  Lots of content type options.  In that way wiki seems like a good
    way to describe it.
    """

    content = StreamField([
        ('rich_text', blocks.RichTextBlock()),
    ])

    stream_panels = [
        StreamFieldPanel('content'),
    ]

    tags = ClusterTaggableManager(through=WikiPageTag, blank=True)

    show_in_news = models.BooleanField(default=False,help_text='Include page in site news: e.g., front page.')

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('show_in_news'),
            FieldPanel('tags'),
        ])
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Heading'),
        ObjectList(stream_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
    ])





