from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase





#class WikiPageFeedBlock(blocks.StructBlock):
#
#    page = blocks.PageChooserBlock(
#        help_text = 'Page to generate freed from.'
#    )
#
#    class Meta:
#        icon = 'user'
#        label = 'Page Feed'
#        # template=''





class WikiPageTag(TaggedItemBase):
    content_object = ParentalKey('wiki.WikiPage', related_name='tagged_items')

class WikiPage(Page):
    """
    Default content type for our site.  No one owns the page.  Anyone can edit
    it.  Lots of content type options.  In that way wiki seems like a good
    way to describe it.
    """

    blurb = models.TextField(
        help_text='Short description of the page.',
    )
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    heading_panels = Page.content_panels + [
        FieldPanel('blurb'),
        ImageChooserPanel('icon'),
    ]

    content = StreamField([
        ('container', blocks.StreamBlock([
            ('rich_text', blocks.RichTextBlock(
                label='Rich Text')),
            ('news_feed', blocks.PageChooserBlock(
                label='News Feed',
                template='wiki/blocks/news_feed.html')),
        #], template='wiki/blocks/container.html')),
        ])),
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
        ObjectList(heading_panels, heading='Heading'),
        ObjectList(stream_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
    ])

    class Meta:
        verbose_name = 'Wiki Page'




