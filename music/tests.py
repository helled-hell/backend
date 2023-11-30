from django.test import TestCase
from .models import Spotik

class MusicTestCase(TestCase):
    def test_model_name(self):
        spotify = Spotik.objects.create(name="song", artist="author")
        self.assertEqual(spotify.name, "song")

    def test_model_url(self):
        spotify = Spotik.objects.create(name="song", artist="author")
        self.assertEqual(spotify.artist, "author")
      # Create your tests here.
