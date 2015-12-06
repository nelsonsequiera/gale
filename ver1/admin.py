from django.contrib import admin
from ver1.models import Article

# attributes to be dispalyed in admi site
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')

# registering the models to the admin
admin.site.register(Article, ArticleAdmin)