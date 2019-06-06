from django.urls import path

from .views import ratings_create_view, find_best_match_view
urlpatterns = [

    path('', ratings_create_view, name = 'durham_fun_finder'),
    path('announce_venue', find_best_match_view, name = 'announce_venue'),
    
]
 