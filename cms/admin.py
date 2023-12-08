from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm, FileField

admin.site.site_header="Portail DCNSI"
admin.site.index_title= "Administration"
admin.site.site_title= "Portail DCNSI"

class ImageModelForm(ModelForm):
    class Meta:
        model = Image()
        exclude = []
        field_classes = {
            'image': FileField,
        }
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class ImageAdmin(admin.ModelAdmin):
    form=ImageModelForm
    list_display = ['image', 'alt_text']
class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','description','start_date','end_date']
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Event, EventAdmin)