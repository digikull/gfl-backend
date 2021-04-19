from django.contrib import admin
from django.urls import path,include
from .views import TournamentView

urlpatterns = [
    path('tournament/',TournamentView.as_view()),
  
]