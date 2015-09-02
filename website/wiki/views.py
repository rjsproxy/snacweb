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




def WikiPageHomeView(request):
    return render(request, 'wiki/home.html')



def WikiPageNewsView(request):
    page_list = WikiPage.objects.filter(show_in_news=True)
    paginator = Paginator(page_list, 3)
    page = request.GET.get('page')

    try:
        page_list = paginator.page(page)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    except:
        page_list = paginator.page(1)

    return render(request, 'wiki/news.html', {'page_list': page_list})




