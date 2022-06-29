from django.urls import path

from films.views import FilmView, FilmDetailView

urlpatterns = [
    path('', FilmView.as_view()),
    path('/<int:film_id>', FilmDetailView.as_view()),
]
