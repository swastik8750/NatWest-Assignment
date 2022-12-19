from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class RpsViewsTestCase(TestCase):
    def test_play_view_with_valid_moves(self):
        """Test the play view with valid player moves."""
        moves = ['rock', 'paper', 'scissors']
        for move in moves:
            url = reverse('play')
            data = {'move': move}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = self.client.post(url, data=data, headers=headers)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn('player_move', response.json())
            self.assertEqual(response.json()['player_move'], move)
            self.assertIn('computer_move', response.json())
            self.assertIn('result', response.json())

    def test_play_view_with_invalid_moves(self):
        """Test the play view with invalid player moves."""
        invalid_moves = ['', 'invalid', 'rock-paper-scissors']
        for move in invalid_moves:
            url = reverse('play')
            data = {'move': move}
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = self.client.post(url, data=data, headers=headers)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_game_logs_view_with_no_games(self):
        """Test the game_logs view with no games."""
        url = reverse('game_logs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])
        
'''
import requests

url = 'http://localhost:8000/RPS/play/'
data = {'move': 'rock'}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url, data=data, headers=headers)
print(response.json())

'''