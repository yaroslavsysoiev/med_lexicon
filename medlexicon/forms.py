from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Word, Category, WordFormat


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = "__all__"
        widgets = {
            'word_format': forms.Select(),
            'category': forms.Select(),
            'worker': forms.Select(),
        }


class WordCreationForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ["text", "translation_uk", "translation_pl", "word_format", "category"]


class WordUpdateForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ["text", "translation_uk", "translation_pl", "word_format", "category"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name"]


class WordFormatForm(forms.ModelForm):
    class Meta:
        model = WordFormat
        fields = ["format_name"]


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")

    # Пример валидации поля, если потребуется
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) < 2:
            raise ValidationError("First name must be at least 2 characters long")
        return first_name


def validate_word_length(text):
    if len(text) < 2:
        raise ValidationError("The word must be at least 2 characters long")
    return text
