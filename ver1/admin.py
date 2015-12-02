from django.contrib import admin
from ver1.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')

# Register your models here.
admin.site.register(Article, ArticleAdmin)