

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class RpsViewsTestCase(TestCase):
    def test_play_view(self):
        url = reverse('play')
        data = {'move': 'rock'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = self.client.post(url, data=data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('player_move', response.json())
        self.assertIn('computer_move', response.json())
        self.assertIn('result', response.json())

    def test_game_logs_view(self):
        url = reverse('game_logs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)
        self.assertGreaterEqual(len(response.json()), 0)


'''
import requests

url = 'http://localhost:8000/RPS/play/'
data = {'move': 'rock'}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url, data=data, headers=headers)
print(response.json())

'''