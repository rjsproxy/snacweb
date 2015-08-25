from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.blocks import StructBlock, ListBlock, PageChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import Tag, TaggedItemBase



#class WikiIndexDisplayBlock(blocks.ChoiceBlock):
#    choices = [
#        ('text-list', 'Text List'),
#        ('icon-list', 'Icon List'),
#    ]
#
#    class Meta:
#        icon = 'cup'




class WikiPageLink(StructBlock):
    """
    Purpose: Combined with ListBlock this class allows editors to create a
    gallery of links to pages.
    """

    page = PageChooserBlock()
    icon = ImageChooserBlock()

    class Meta:
        icon = 'cup'


class WikiPageTag(TaggedItemBase):
    content_object = ParentalKey('wiki.WikiPage', related_name='tagged_items')

class WikiPage(Page):
    """
    Default content type for our site.  No one owns the page.  Anyone can edit
    it.  Lots of content type options.  In that way wiki seems like a good
    way to describe it.
    """

    content = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('background', ImageChooserBlock()),
        ('navigation', ListBlock(WikiPageLink)),
    ])

    stream_panels = [
        StreamFieldPanel('content'),
    ]

    tags = ClusterTaggableManager(through=WikiPageTag, blank=True)

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Heading'),
        ObjectList(stream_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
    ])

