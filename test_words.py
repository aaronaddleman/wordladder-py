from words import wordLadder
from unittest import TestCase

class wordLadderTest(TestCase):
  def test_word_accepted(self):
    wl = wordLadder("hit", "cog", ["hot", "dot", "dog", "log", "cog"])
    wl.beginWord = "hit"
  def test_word_length(self):
    wl = wordLadder("hit", "cog", ["hot", "dot", "dog", "log", "cog"])
    self.assertTrue(wl.wordLength("hit"))
    self.assertFalse(wl.wordLength("wordtoolong"))
