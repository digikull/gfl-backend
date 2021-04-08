
from django.urls import path
from . import views 

urlpatterns = [

    path('player-list/', views.get_all_players),
	path('player-create/', views.create_player, name="create_player"),
	path('player-update/<int:pk>/', views.update_player, name="update_player"),
	path('player-delete/<int:pk>/', views.delete_player, name="delete_player"),
	path('player/<int:pk>/', views.get_player),
]
