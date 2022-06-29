from django.urls import path

from films.views import FilmDetailView

urlpatterns = [
    path('/<int:film_id>', FilmDetailView.as_view()),
]