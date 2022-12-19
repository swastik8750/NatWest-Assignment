from django.db import models

class Game(models.Model):
    player_move = models.CharField(max_length=10)
    computer_move = models.CharField(max_length=10)
    result = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)