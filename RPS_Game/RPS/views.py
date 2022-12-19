import random

from rest_framework import views
from rest_framework.response import Response

from .models import Game

from .serializers import GameSerializer


class PlayView(views.APIView):
    def post(self, request):
        player_move = request.data['move']
        computer_move = get_random_move()
        result = get_winner(player_move, computer_move)
        game = Game.objects.create(player_move=player_move, computer_move=computer_move, result=result)
        serializer = GameSerializer(game)
        return Response(serializer.data)

def get_random_move():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It is a tie"
    elif player_move == 'rock' and computer_move == 'scissors':
        return "Player wins"
    elif player_move == 'scissors' and computer_move == 'paper':
        return "Player wins"
    elif player_move == 'paper' and computer_move == 'rock':
        return "Player wins"
    else:
        return "Computer wins"

class GameLogsView(views.APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


# postman link : https://elements.getpostman.com/redirect?entityId=21892039-088c025a-c6f6-44bd-ad51-22ea61037009&entityType=collection