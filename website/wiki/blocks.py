from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.html import format_html

from markdown import markdown

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore import hooks



class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block

    Originally from https://gist.github.com/frankwiles/74a882f16704db9caa27


    The biggest problem here is that we cannot easily provide page links.

    """
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='default',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))


class MarkDownBlock(blocks.TextBlock):
    """
    MarkDown Block
    
    See http://pythonhosted.org/Markdown/extensions/index.html for extensions.
    
    Originally from https://gist.github.com/frankwiles/74a882f16704db9caa27
    """

    class Meta:
        icon = 'code'

    def render_basic(self, value):
        md = markdown(
            value,
            [
                'markdown.extensions.fenced_code',
                'markdown.extensions.tables',
                'codehilite',
            ],
        )
        return mark_safe(md)




#class SingleImageBlock(blocks.ImageChooserBlock)
#    
#    DISPLAY_CHOICES = (
#        ('left', 'Left Align'),
#        ('middle', 'Center'),
#        ('righ', 'Right'),
#    )


# the following possibly should define wiki_admin.css and provide for all blocks.

@hooks.register('insert_editor_css')
def markdown_editor_css():
    return format_html('<link rel="stylesheet" href="' \
    + settings.STATIC_URL + 'wiki/wagtail/markdown.css">')
