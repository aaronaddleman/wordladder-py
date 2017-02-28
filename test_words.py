from words import wordLadder
from unittest import TestCase

class wordLadderTest(TestCase):
  def test_word_accepted(self):
    wl = wordLadder()
    wl.beginWord = "hit"
  def test_word_length(self):
    wl = wordLadder()
    wl.wordLength("hit")
