# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article, Category, Tag

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract', 'category', 'created')
    list_per_page = 50
    ordering = ('-created',)
    list_filter = ('category','tags')
    search_fields = ('title',)
    filter_horizontal = ('tags',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
