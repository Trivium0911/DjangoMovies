from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Movie


class MovieView(ListView):
    """Movie list"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    """Full movie description"""
    model = Movie
    slug_field = "url"


class AddReview(View):
    """Review"""
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")
