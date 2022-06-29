from django.urls import path

from films.views import FilmView

urlpatterns = [
    path('', FilmView.as_view()),
]
