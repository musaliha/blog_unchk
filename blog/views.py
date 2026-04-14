from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Q
from .models import Article


# 🔵 LISTE DES ARTICLES
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    context_object_name = 'articles'
    ordering = ['-id']  # 🔥 afficher les plus récents en premier


# 🔵 DETAIL
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'  # 🔥 plus propre dans le template


# 🟢 CREATION
class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'blog/form.html'
    success_url = reverse_lazy('list')


# 🟡 MODIFICATION
class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'blog/form.html'
    success_url = reverse_lazy('list')


# 🔴 SUPPRESSION
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('list')


# 🔍 RECHERCHE (AJOUTÉE)
def search(request):
    query = request.GET.get('q', '').strip()

    if query:
        results = Article.objects.filter(
            Q(titre__icontains=query) |
            Q(contenu__icontains=query) |
            Q(auteur__icontains=query)
        )
    else:
        results = Article.objects.none()

    return render(request, 'blog/search.html', {
        'results': results,
        'query': query
    })