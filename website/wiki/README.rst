
ReadMe
======


Putting some things here which might be useful in the future.

from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.wagtailcore.blocks import StructBlock, ListBlock, PageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock
from taggit.models import Tag, TaggedItemBase
from .fields import LinkField



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




#class WikiIndexDisplayBlock(blocks.ChoiceBlock):
#    choices = [
#        ('text-list', 'Text List'),
#        ('icon-list', 'Icon List'),
#    ]
#
#    class Meta:
#        icon = 'cup'





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


class ImageThumbBlock(StructBlock):
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

    class Meta:
        template = 'wiki/blocks/thumbnail_image.html'


class PageThumbBlock(ImageThumbBlock):
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'wiki/blocks/thumbnail_page.html'


class ColumnChoiceBlock(blocks.ChoiceBlock):

    choices = [
        (2, 'Two Columns'),
        (3, 'Three Columns'),
    ]

    class Meta:
        icon = 'cogs'


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





        ('row', blocks.StructBlock([
            ('column_number', ColumnChoiceBlock()),
            ('column_content', blocks.StreamBlock([
                    ('image', ImageThumbBlock()),
                    ('page', PageThumbBlock()),
                ], template='wiki/blocks/thumbnail_stream.html')),
            ], template='wiki/blocks/row_block.html'),
        ),
        #('image', ImageChooserBlock()),
        #('service', ListBlock(SnippetChooserBlock(Service), template='wiki/blocks/wiki_service_list.html')),
        #('background', ImageChooserBlock()),
        #('navigation', ListBlock(WikiPageLink, template='wiki/blocks/wiki_page_list.html')),  # pageiconlist
        #('page_feed', PageChooserBlock(template='wiki/blocks/wiki_page_feed.html')),
