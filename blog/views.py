from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'blog/form.html'
    success_url = reverse_lazy('list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'blog/form.html'
    success_url = reverse_lazy('list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('list')