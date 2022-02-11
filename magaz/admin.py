from django.contrib import admin

from magaz.models import ArticleCategory, Article


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
   pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass