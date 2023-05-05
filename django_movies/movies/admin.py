from django.contrib import admin
from .models import Actor, Category, Genre, Movie, MovieScreen, Rating, \
    RatingStar, Reviews


admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieScreen)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
