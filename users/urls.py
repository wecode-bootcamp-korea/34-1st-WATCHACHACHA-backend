from django.urls import path

from users.views import SignUpView, SignInView, WatchListView, UserView
urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/watchlist', WatchListView.as_view()),
    path('/profile', UserView.as_view()),
]
