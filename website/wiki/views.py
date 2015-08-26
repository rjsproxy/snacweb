from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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



