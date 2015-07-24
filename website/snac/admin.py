from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import Service, BlogPost

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Service, ServiceAdmin)


class BlogPostAdmin(admin.ModelAdmin):

    list_display = ('title','created','modified')
    prepopulated_fields = {'slug': ('title',), }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Select the user who is currently logged in.
        """
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(BlogPost, BlogPostAdmin)

# 
# Overide django-flatpages text field to use CKEditor.
#
# http://stackoverflow.com/questions/14864642/how-to-integrate-wysiwyg-editor-with-django-flatpages

class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)


