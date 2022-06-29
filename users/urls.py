from django.urls import path

from users.views import SignUpView, SignInView, WatchListView, ProfileView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/watchlist/<int:film_id>', WatchListView.as_view()),
    path('/profile/<int:user_id>', ProfileView.as_view()),
]
