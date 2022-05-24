from django.shortcuts import get_object_or_404
from .models import Movie, Category
from django.views.generic import ListView, DetailView


# Create your views here.
class HomeListView(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 1
    template_name = 'mov/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class MovieTypeView(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 1
    template_name = 'mov/home.html'
    type = None

    def get_queryset(self):
        self.type = get_object_or_404(Movie, type=self.kwargs['type'])
        return Movie.objects.filter(type=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['type'] = self.type
        return context


class CategoryListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'mov/home.html'
    category = None

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.kwargs['category'])
        return Movie.objects.filter(category__name=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context


class MovieDetailView(ListView):
    model = Movie
    template_name = 'mov/detail.html'
    movie = None

    def get_queryset(self):
        self.movie = get_object_or_404(Movie, type=self.kwargs['type'], slug=self.kwargs['slug'],
                                       production=self.kwargs['production'])

        return self.movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = self.movie
        context['categories'] = Category.objects.all()
        return context
