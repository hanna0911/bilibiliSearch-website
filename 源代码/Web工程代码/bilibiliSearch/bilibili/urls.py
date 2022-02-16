from django.urls import path
from bilibili import views, tests


urlpatterns = [
    path('movielist/', views.movielist),
    path('userlist/', views.userlist),
    path('movielist/movie/<movieID>/', views.movie),
    path('userlist/user/<userID>', views.user),
]