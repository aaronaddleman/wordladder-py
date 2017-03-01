from words import wordLadder
from unittest import TestCase
import re

class wordLadderTest(TestCase):
  def setUp(self):
    self.wl = wordLadder("hit", "cog", ["hot", "dot", "dog", "log", "cog"])
  def test_beingWord_accepted(self):
    self.assertEqual("hit", self.wl.beginWord)
  def test_endWord_accepted(self):
    self.assertEqual("cog", self.wl.endWord)
  def test_word_length(self):
    self.assertTrue(self.wl.wordLength("hit"))
    self.assertFalse(self.wl.wordLength("wordtoolong"))
  def test_wordDiff(self):
    self.assertListEqual(self.wl.wordDiff(self.wl.beginWord, self.wl.endWord),
                         ['- h', '- i', '- t', '+ c', '+ o', '+ g'])
  def test_nextWord(self):
    self.assertEqual(self.wl.nextWord(), "hot")
