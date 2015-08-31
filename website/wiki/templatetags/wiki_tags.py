from django import template
from wiki.models import *

register = template.Library()

#
# From back in the day when we had service snippets.
#
#
# @register.inclusion_tag('wiki/tags/service.html', takes_context=True)
#def adverts(context):
#    return {
#        'services': Advert.objects.all(),
#        'request': context['request'],
#    }


