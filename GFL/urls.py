
from django.urls import path
from . import views
urlpatterns = [
    path('tournamentapi/',views.ListTournament.as_view())
]
