from django.db import models
from django.utils import timezone


class ArticleCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'категория'  # эти названия будут показывать в админ панели
        verbose_name_plural = 'категории'
        ordering=['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    """Модель для публикации"""
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(to=ArticleCategory, on_delete=models.CASCADE,
                                 related_name='articles')  # related_name - для обращения из категории к публикациям
    image = models.ImageField(default=None)
    is_new=models.BooleanField(default=False)
    created_at = models.DateTimeField(default = timezone.now())
    updated_at = models.DateTimeField(default = timezone.now())


    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'Публикации'
        ordering = ['title']


    def __str__(self):
        return self.title

#
# class ArticleTag(models.Model):
#     """Модель хэштега для публикаций"""
#     title = models.CharField(max_length=100, unique=True)
#     article = models.ManyToManyField(to=Article)
#
#     class Meta:
#         verbose_name = 'Хэштег публикация'
#         verbose_name_plural = 'Хэштеги публикации'
#
#     def __str__(self):
#         return self.title
#
#
# class ArticleComment(models.Model):
#     article = models.ForeignKey(to=Article, related_name='comments',on_delete=models.CASCADE)
#     text = models.TextField()
#
#
#     class Meta:
#         verbose_name_plural = 'каментарии к публикации'
#         verbose_name = 'каментарии публикациям'
#
#
#     def __str__(self):
#         return self.text


