import datetime

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import Service, BlogPost


class LandingView(TemplateView):

    template_name = 'snac/landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['service_list'] = Service.objects.all();
        context['blogpost_list'] = BlogPost.objects.order_by('-created')[:5]
        return context;



class ServiceDetailView(DetailView):

    model = Service




class BlogPostDetailView(DetailView):

    model = BlogPost

    def get_object(self):
        return get_object_or_404(BlogPost,
            created__year = int(self.kwargs['year']),
            created__month = int(self.kwargs['month']),
            created__day = int(self.kwargs['day']),
            slug=self.kwargs['slug'])

    





