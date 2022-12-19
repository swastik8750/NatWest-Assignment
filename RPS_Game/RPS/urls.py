

from django.urls import path
from . import views

urlpatterns = [
    path('play/', views.PlayView.as_view(), name='play'),
    path('games/', views.GameLogsView.as_view(), name='game_logs'),
]
