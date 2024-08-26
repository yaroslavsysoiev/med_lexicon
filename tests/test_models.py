from django.test import TestCase
from django.urls import reverse

from medlexicon.models import Word, Category, WordFormat, Worker


class ModelsTests(TestCase):

    def test_worker_str(self):
        worker = Worker.objects.create_user(
            username="worker1",
            password="password123",
            first_name="Worker",
            last_name="One",
            phone_number="1234567890"
        )
        self.assertEqual(
            str(worker),
            f"{worker.username} ({worker.first_name} {worker.last_name})"
        )

    def test_category_str(self):
        category = Category.objects.create(
            category_name="Medical Terms"
        )
        self.assertEqual(str(category), category.category_name)

    def test_word_format_str(self):
        word_format = WordFormat.objects.create(
            format_name="Noun"
        )
        self.assertEqual(str(word_format), word_format.format_name)

    def test_word_str(self):
        category = Category.objects.create(
            category_name="Medical Terms"
        )
        word_format = WordFormat.objects.create(
            format_name="Noun"
        )
        worker = Worker.objects.create_user(
            username="worker2",
            password="password123",
            first_name="Worker",
            last_name="Two",
            phone_number="0987654321"
        )
        word = Word.objects.create(
            text="Medicine",
            translation_uk="Ліки",
            translation_pl="Lekarstwo",
            category=category,
            word_format=word_format,
            worker=worker
        )
        self.assertEqual(str(word), word.text)

    def test_worker_get_absolute_url(self):
        worker = Worker.objects.create_user(
            username="worker3",
            password="password123",
            first_name="Worker",
            last_name="Three",
            phone_number="1122334455"
        )
        expected_url = reverse("medlexicon:worker-detail", kwargs={"pk": worker.pk})
        self.assertEqual(worker.get_absolute_url(), expected_url)

    def test_word_has_worker(self):
        category = Category.objects.create(
            category_name="Medical Terms"
        )
        word_format = WordFormat.objects.create(
            format_name="Noun"
        )
        worker = Worker.objects.create_user(
            username="worker6",
            password="password123",
            first_name="Worker",
            last_name="Six",
            phone_number="6677889900"
        )
        word = Word.objects.create(
            text="Health",
            translation_uk="Здоров'я",
            translation_pl="Zdrowie",
            category=category,
            word_format=word_format,
            worker=worker
        )
        self.assertEqual(word.worker, worker)
