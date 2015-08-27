from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import WikiPage


# generate page feed/list by url/tag.

from django.template.response import TemplateResponse

def WikiPageEventView(request):

    content_list = WikiPage.objects.all()
    paginator = Paginator(content_list, 5)
    page = request.GET.get('page')

    try:
        content = paginator.page(page)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)
    except:
        content = paginator.page(1)

    return render(request, 'wiki/page_feed.html', {'content': content})



def WikiPageTagView(request, tag_list=[]):
    """
    Select pages with the given tags and order by newest to oldest.
    """
    page_list = None
    if tag_list:
        q_list = Q(tags__name=tag_list[0])
        for tag in tag_list[1:]:
            q_list |= Q(tags__name=tag)
        page_list = WikiPage.objects.filter(q_list).order_by('-first_published_at')
    return render(request, 'wiki/tag_view.html', {'page_list': page_list})



