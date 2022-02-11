from django.shortcuts import render

from django.http import Http404
from django.views import generic
from magaz.models import ArticleCategory, Article


class BlogView(generic.TemplateView):
    """Представление для получения всех публикаций"""
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['category_list'] = ArticleCategory.objects.all()
        context['article_list'] = Article.objects.all()
        return context


class BlogDetailView(generic.TemplateView):
    template_name = 'single.html'

    def get_context_data(self, **kwargs):
        context = dict()
        category_pk = kwargs['category_pk']
        context['category_list'] = ArticleCategory.objects.all()
        context['article_list'] = Article.objects.filter(category_id=category_pk)
        return context

