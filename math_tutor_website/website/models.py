from enum import unique

from django.db import models
from django.urls import reverse


class Publications(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="image/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='get_programs')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program', kwargs={'program_slug': self.slug})

    class Meta:
        verbose_name = 'Публикации'
        verbose_name_plural = 'Публикации'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True,  verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class About(models.Model):
    name = models.CharField(max_length=255, db_index=True,  verbose_name='Название раздела')
    about = models.CharField(max_length=255, db_index=True,  verbose_name='О сайте')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'О сайте'
        verbose_name_plural = 'О сайте'
