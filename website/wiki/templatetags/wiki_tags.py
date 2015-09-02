from django import template
from django.core.paginator import Paginator

from wiki.models import WikiPage

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


@register.assignment_tag(takes_context=True)
def wiki_root(context):                                                                               
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ                              
    return context['request'].site.root_page   

def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('wiki/menu.html', takes_context=True)
def wiki_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('wiki/menu_children.html', takes_context=True)
def wiki_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



@register.inclusion_tag('wiki/tags/news_feed.html')
def news_feed(root_page, feed_items=20, feed_index=1):
    page_list = WikiPage.objects.live().filter(show_in_news=True).descendant_of(root_page).order_by('-first_published_at')
    paginator = Paginator(page_list, feed_items)

    try:
        page_list = paginator.page(feed_index)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    except:
        page_list = paginator.page(1)

    return {
        'page_list': page_list,
        #'request': context['request'],
    }

