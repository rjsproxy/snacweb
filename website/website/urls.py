from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from wiki.views import WikiPageEventView, WikiPageTagView, WikiPageHomeView, WikiPageNewsView

urlpatterns = [
    url(r'^django/', include(admin.site.urls)),
    url(r'^wagtail/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    #url(r'^search/$', 'search.views.search', name='search'),  #,  from demo, menu

    url(r'^$', WikiPageHomeView),
    #url(r'^news/', WikiPageNewsView),

    #url(r'^events/', WikiPageEventView),
    #url(r'^tags/', WikiPageTagView, {'tag_list': ['service']}),

    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

