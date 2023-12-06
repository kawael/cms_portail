from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.site_header="Portail DCNSI"
admin.site.index_title= "Administration"
admin.site.site_title= "Portail DCNSI"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'alt_text']
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)