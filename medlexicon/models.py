from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Worker(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("medlexicon:worker-detail", kwargs={"pk": self.pk})


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
    translation_uk = models.CharField(max_length=200)
    translation_pl = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word_format = models.ForeignKey(WordFormat, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
