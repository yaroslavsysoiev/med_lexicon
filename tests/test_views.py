from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from medlexicon.models import Word, Category, WordFormat

INDEX_URL = reverse("medlexicon:index")
CATEGORY_LIST_URL = reverse("medlexicon:category-list")
WORD_FORMAT_LIST_URL = reverse("medlexicon:wordformat-list")
WORD_LIST_URL = reverse("medlexicon:word-list")
WORKER_LIST_URL = reverse("medlexicon:worker-list")
WORD_CREATE_URL = reverse("medlexicon:word-create")


class PublicMedlexiconTests(TestCase):
    def test_login_required_category_list(self):
        res = self.client.get(CATEGORY_LIST_URL)
        self.assertNotEqual(res.status_code, 200)
        self.assertRedirects(res, f"/accounts/login/?next={CATEGORY_LIST_URL}")

    def test_login_required_word_format_list(self):
        res = self.client.get(WORD_FORMAT_LIST_URL)
        self.assertNotEqual(res.status_code, 200)
        self.assertRedirects(res, f"/accounts/login/?next={WORD_FORMAT_LIST_URL}")

    def test_login_required_worker_list(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(res.status_code, 200)
        self.assertRedirects(res, f"/accounts/login/?next={WORKER_LIST_URL}")

    def test_login_required_word_create(self):
        res = self.client.get(WORD_CREATE_URL)
        self.assertNotEqual(res.status_code, 200)
        self.assertRedirects(res, f"/accounts/login/?next={WORD_CREATE_URL}")


class PrivateCategoryTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client.force_login(self.user)

    def test_retrieve_categories(self):
        Category.objects.create(category_name="Medical Terms")
        Category.objects.create(category_name="Legal Terms")

        response = self.client.get(CATEGORY_LIST_URL)

        self.assertEqual(response.status_code, 200)
        categories = Category.objects.all()
        self.assertEqual(
            list(response.context["category_list"]),
            list(categories),
        )
        self.assertTemplateUsed(response, "medlexicon/category_list.html")


class PrivateWordFormatTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client.force_login(self.user)

    def test_retrieve_word_formats(self):
        WordFormat.objects.create(format_name="Noun")
        WordFormat.objects.create(format_name="Verb")

        response = self.client.get(WORD_FORMAT_LIST_URL)

        self.assertEqual(response.status_code, 200)
        word_formats = WordFormat.objects.all()
        self.assertEqual(
            list(response.context["wordformat_list"]),
            list(word_formats),
        )
        self.assertTemplateUsed(response, "medlexicon/wordformat_list.html")


class PrivateWordTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client.force_login(self.user)

    def test_retrieve_words(self):
        category = Category.objects.create(category_name="Medical Terms")
        word_format = WordFormat.objects.create(format_name="Noun")
        word = Word.objects.create(
            text="Health",
            translation_uk="Здоров'я",
            translation_pl="Zdrowie",
            category=category,
            word_format=word_format,
            worker=self.user
        )

        response = self.client.get(WORD_LIST_URL)

        self.assertEqual(response.status_code, 200)
        words = Word.objects.all()
        self.assertEqual(
            list(response.context["word_list"]),
            list(words),
        )
        self.assertTemplateUsed(response, "medlexicon/word_list.html")

    def test_word_create(self):
        category = Category.objects.create(category_name="Medical Terms")
        word_format = WordFormat.objects.create(format_name="Noun")

        response = self.client.post(WORD_CREATE_URL, {
            "text": "Medicine",
            "translation_uk": "Медицина",
            "translation_pl": "Medycyna",
            "category": category.id,
            "word_format": word_format.id
        })

        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(Word.objects.filter(text="Medicine").exists())
