from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Worker, Word, Category, WordFormat
from .forms import WordCreationForm, WordUpdateForm, CategoryForm, WordFormatForm, WorkerCreationForm, \
    WorkerPhoneUpdateForm


def index(request):
    """View function for the home page of the site."""

    num_words = Word.objects.count()
    num_categories = Category.objects.count()
    num_word_formats = WordFormat.objects.count()
    num_workers = Worker.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_words": num_words,
        "num_categories": num_categories,
        "num_word_formats": num_word_formats,
        "num_workers": num_workers,
        "num_visits": num_visits + 1,
    }

    return render(request, "medlexicon/index.html", context=context)


class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "medlexicon/category_list.html"
    paginate_by = 5


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("medlexicon:category-list")


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Category
    template_name = "medlexicon/category_detail.html"


class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    fields = ['category_name']
    template_name = 'medlexicon/category_form.html'
    success_url = reverse_lazy("medlexicon:category-list")


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = "medlexicon/category_confirm_delete.html"
    success_url = reverse_lazy("medlexicon:category-list")


class WordFormatListView(LoginRequiredMixin, generic.ListView):
    model = WordFormat
    context_object_name = "wordformat_list"
    template_name = "templates/medlexicon/wordformat_list.html"
    paginate_by = 5


class WordFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = WordFormat
    form_class = WordFormatForm
    success_url = reverse_lazy("medlexicon:wordformat-list")


class WordFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = WordFormat
    form_class = WordFormatForm
    success_url = reverse_lazy("medlexicon:wordformat-list")


class WordFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = WordFormat
    success_url = reverse_lazy("medlexicon:wordformat-list")


class WordListView(LoginRequiredMixin, generic.ListView):
    model = Word
    paginate_by = 10
    queryset = Word.objects.select_related("word_format", "category", "worker")
    success_url = reverse_lazy("medlexicon:wordformat-list")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Word.objects.filter(text__icontains=query)
        return super().get_queryset()


class WordDetailView(LoginRequiredMixin, generic.DetailView):
    model = Word
    template_name = "medlexicon/word_detail.html"


class WordCreateView(LoginRequiredMixin, generic.CreateView):
    model = Word
    form_class = WordCreationForm
    success_url = reverse_lazy("medlexicon:word-list")

    def form_valid(self, form):
        form.instance.worker = self.request.user
        return super().form_valid(form)


class WordUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Word
    form_class = WordUpdateForm
    success_url = reverse_lazy("medlexicon:word-list")


class WordDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Word
    success_url = reverse_lazy("medlexicon:word-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5
    context_object_name = "worker_list"
    template_name = "medlexicon/worker_list.html"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    context_object_name = "worker"
    template_name = "medlexicon/worker_detail.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = "medlexicon/worker_form.html"
    success_url = reverse_lazy("medlexicon:worker-list")


class WorkerPhoneUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerPhoneUpdateForm
    success_url = reverse_lazy("medlexicon:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("medlexicon:worker-list")


@login_required
def toggle_assign_to_category(request, pk):
    word = Word.objects.get(id=pk)
    category = Category.objects.get(id=request.POST["category_id"])

    if word.category == category:
        word.category = None
    else:
        word.category = category

    word.save()
    return HttpResponseRedirect(reverse_lazy("words:word-detail", args=[pk]))
