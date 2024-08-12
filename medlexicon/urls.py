from django.urls import path

from . import views
from medlexicon.views import (
    index,
    WordListView,
    WordDetailView,
    WordCreateView,
    WordUpdateView,
    WordDeleteView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    WordFormatListView,
    WordFormatCreateView,
    WordFormatUpdateView,
    WordFormatDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("words/", WordListView.as_view(), name="word-list"),
    path("words/<int:pk>/", WordDetailView.as_view(), name="word-detail"),
    path("words/create/", WordCreateView.as_view(), name="word-create"),
    path("words/<int:pk>/update/", WordUpdateView.as_view(), name="word-update"),
    path("words/<int:pk>/delete/", WordDeleteView.as_view(), name="word-delete"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/update/", CategoryUpdateView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
    path("wordformats/", WordFormatListView.as_view(), name="wordformat-list"),
    path("wordformats/create/", WordFormatCreateView.as_view(), name="wordformat-create"),
    path("wordformats/<int:pk>/update/", WordFormatUpdateView.as_view(), name="wordformat-update"),
    path("wordformats/<int:pk>/delete/", WordFormatDeleteView.as_view(), name="wordformat-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
]

app_name = "medlexicon"
