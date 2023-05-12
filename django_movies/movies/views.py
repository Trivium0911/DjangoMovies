from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Movie


class MovieView(View):
    """Movie list"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    """Full movie description"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})
