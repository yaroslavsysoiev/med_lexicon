from django.db import models
from django.contrib.auth.models import AbstractUser


class Worker(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class WordFormat(models.Model):
    format_name = models.CharField(max_length=100)

    def __str__(self):
        return self.format_name


class Word(models.Model):
    text = models.CharField(max_length=200)
    translation_uk = models.CharField(max_length=200)  # Перевод на украинский
    translation_pl = models.CharField(max_length=200)  # Перевод на польский
    date_added = models.DateTimeField(auto_now_add=True)
    word_format = models.ForeignKey(WordFormat, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
