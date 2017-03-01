from words import wordLadder
from unittest import TestCase

class wordLadderTest(TestCase):
  def test_beingWord_accepted(self):
    wl = wordLadder("hit", "cog", ["hot", "dot", "dog", "log", "cog"])
    wl.beginWord = "hit"
    self.assertEqual("hit", wl.beginWord)
  def test_endWord_accepted(self):
    wl = wordLadder("hit", "cog", ["hot", "dot", "dog", "log", "cog"])
    wl.endWord = "cog"
    self.assertEqual("cog", wl.endWord)
  def test_word_length(self):
    wl = wordLadder("hit", "cog", ["hot", "dot", "dog", "log", "cog"])
    self.assertTrue(wl.wordLength("hit"))
    self.assertFalse(wl.wordLength("wordtoolong"))
