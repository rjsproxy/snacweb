from django.db import models


from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.blocks import StructBlock, ListBlock, PageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel
#from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from taggit.models import Tag, TaggedItemBase

from .fields import LinkField

#class WikiIndexDisplayBlock(blocks.ChoiceBlock):
#    choices = [
#        ('text-list', 'Text List'),
#        ('icon-list', 'Icon List'),
#    ]
#
#    class Meta:
#        icon = 'cup'


@register_snippet
class Service(LinkField):
    """
    A collection of links to SNAC services.  Using a URL field allows these
    links to go to any destination.
    """

    name = models.CharField(max_length=64)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
        MultiFieldPanel(LinkField.panels, 'Link'),
    ]

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



class LinkBlock(StructBlock):

    page = PageChooserBlock(
        help_text='Link to page on this site.',
        required=False,
    )
    document = DocumentChooserBlock(
        help_text='Link to document on this site.',
        required=False,
    )
    external = blocks.URLBlock(
        help_text='Link to external URL.',
        required=False,
    )

    @property
    def url(self):
        if self.page:
            return self.page.url
        elif self.document:
            return self.document.url
        else:
            return self.external

    def party(self):
        return dir(self)
        return "<p>Oh, yeah, party!</p>"

    class Meta:
        template = 'wiki/blocks/link.html'


class ThumbBlock(StructBlock):
    """
    Field for creating a Bootstrap thumnail.
    """

    title = blocks.CharBlock(
        help_text='Title for thumnail.'
    )
    caption = blocks.TextBlock(
        help_text='Thumbnail description shown if space permits.',
        required=False,
    )
    image = ImageChooserBlock(
        help_text='Image to show in thumbnail.',
    )
    link = LinkBlock(
        help_text='Link to associate with this Thumbnail.',
    )



    #panels = [
    #    FieldPanel('title'),
    #    FieldPanel('caption'),
    #    blocks.ImageChooserPanel('image'),
    #    MultiFieldPanel(LinkField.panels, 'link'),
    #]

    class Meta:
        #default =
        icon = 'user'
        #icon =
        #template = 

    def __unicode__(self):
        return self.title




class WikiPageLink(StructBlock):
    """
    Purpose: Combined with ListBlock this class allows editors to create a
    gallery of links to pages.
    """

    page = PageChooserBlock()
    icon = ImageChooserBlock()

    class Meta:
        icon = 'cup'
        # template = 'wiki/blocks/wiki_page_link.html'


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
        ('thumbnails', ListBlock(ThumbBlock, template='wiki/blocks/thumbnail_list.html')),
        #('image', ImageChooserBlock()),
        #('service', ListBlock(SnippetChooserBlock(Service), template='wiki/blocks/wiki_service_list.html')),
        #('background', ImageChooserBlock()),
        #('navigation', ListBlock(WikiPageLink, template='wiki/blocks/wiki_page_list.html')),  # pageiconlist
        #('page_feed', PageChooserBlock(template='wiki/blocks/wiki_page_feed.html')),
    ])

    stream_panels = [
        StreamFieldPanel('content'),
    ]

    tags = ClusterTaggableManager(through=WikiPageTag, blank=True)
    show_in_feed = models.BooleanField(default=False,help_text='Include page in site feeds: e.g., front page.')

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('show_in_feed'),
            FieldPanel('tags'),
        ])
    ]


    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Heading'),
        ObjectList(stream_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
    ])





