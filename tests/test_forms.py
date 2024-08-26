from django.test import TestCase
from medlexicon.models import Word, Category, WordFormat, Worker
from medlexicon.forms import (
    WordUpdateForm,
    CategoryForm,
    WordFormatForm,
    WorkerCreationForm,
    WorkerPhoneUpdateForm
)


class FormTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker.objects.create_user(
            username="testworker",
            password="testpassword",
            first_name="John",
            last_name="Doe",
            phone_number="1234567890"
        )
        self.category = Category.objects.create(
            category_name="Medical Terms"
        )
        self.word_format = WordFormat.objects.create(
            format_name="Noun"
        )
        self.word = Word.objects.create(
            text="Medicine",
            translation_uk="Ліки",
            translation_pl="Lekarstwo",
            category=self.category,
            word_format=self.word_format,
            worker=self.worker
        )

    def test_word_update_form_valid(self):
        form_data = {
            "text": "Updated Medicine",
            "translation_uk": "Оновлені ліки",
            "translation_pl": "Zaktualizowane lekarstwo",
            "word_format": self.word_format.id,
            "category": self.category.id
        }
        form = WordUpdateForm(instance=self.word, data=form_data)
        self.assertTrue(form.is_valid())
        updated_word = form.save()
        self.assertEqual(updated_word.text, "Updated Medicine")

    def test_category_form_valid(self):
        form_data = {"category_name": "Anatomy"}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())
        category = form.save()
        self.assertEqual(category.category_name, "Anatomy")

    def test_word_format_form_valid(self):
        form_data = {"format_name": "Verb"}
        form = WordFormatForm(data=form_data)
        self.assertTrue(form.is_valid())
        word_format = form.save()
        self.assertEqual(word_format.format_name, "Verb")

    def test_worker_creation_form_invalid(self):
        form_data = {
            "username": "invalid_worker",
            "password1": "password1234",
            "password2": "differentpassword",  # Passwords do not match
            "first_name": "Alice",
            "last_name": "Smith"
        }
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_worker_phone_update_form_valid(self):
        form_data = {"phone_number": "0987654321"}
        form = WorkerPhoneUpdateForm(instance=self.worker, data=form_data)
        self.assertTrue(form.is_valid())
        updated_worker = form.save()
        self.assertEqual(updated_worker.phone_number, "0987654321")

    def test_worker_phone_update_form_invalid(self):
        form_data = {"phone_number": "123"}  # Too short phone number
        form = WorkerPhoneUpdateForm(instance=self.worker, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("phone_number", form.errors)
