from django.urls import path
from .views import takeUserInputView, findBestMatchView

urlpatterns = [
    path('', takeUserInputView, name = 'durham_fun_finder'),
    path('announce_business', findBestMatchView, name = 'announce_business'),
    ] 