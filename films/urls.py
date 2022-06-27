from django.urls import path

from films.views import FilmMainView

urlpatterns = [
    path('/main', FilmMainView.as_view()),
]
