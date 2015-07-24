from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ckeditor.fields import RichTextField

#from sorl.thumbnail import ImageField # thumbnailing feels like a front-end concern.
#icon = ImageField(upload_to='snac/icons/%Y-%m-%d/')
#icon = models.ImageField(upload_to='snac/icons/%Y/%m/%d/')
#icon = models.ImageField(upload_to='d')
#icon = FilerImageField(null=True, blank=True, related_name="service_icon")

# class Article()
# ckeditor doesn't allow file uploads.
# ckeditor

class Service(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    icon = models.ImageField(upload_to='snac/service/icons/')
    url = models.URLField(blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.slug;

    def get_absolute_url(self):
        if self.url:
            return self.url
        return "/service/%s/" % self.slug

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified =  models.DateTimeField(auto_now=True)
    blurb = models.TextField(max_length=140)
    content = RichTextField(blank=True)

    def __str__(self):
        return self.slug;

    def get_absolute_url(self):
        return "/blogpost/%04d/%02d/%02d/%s/" % (
            self.created.year,
            self.created.month,
            self.created.day,
            self.slug)

    def get_age_string(self):

        diff = timezone.now() - self.created

        years = diff.days / 365
        if years:
            return "%d year%s" % (years, 's' if years != 1 else '')

        weeks = diff.days / 7
        if weeks:
            return "%d week%s" % (weeks, 's' if weeks != 1 else '')

        hours = (diff.seconds / 60) / 60
        if hours > 0:
            return "%d hour%s" % (hours, 's' if hours != 1 else '')
    
        minutes = (diff.seconds / 60)
        if minutes > 0:
            return "%d minute%s" % (minutes, 's' if minutes != 1 else '')

        return "%d second%s" % (diff.seconds, 's' if diff.seconds != 1 else '')


#class FlatPage()
