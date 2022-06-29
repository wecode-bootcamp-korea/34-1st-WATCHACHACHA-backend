from django.urls import path

from users.views import SignUpView, SignInView, WatchListView
urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/watchlist', WatchListView.as_view()),
]
