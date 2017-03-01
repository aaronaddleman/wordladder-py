"""
wordLadder

Given two words, beginWord and endWord, and the wordList of approved
words, find the length of the shortest transformation sequence from
beginWord to endWord such that:

* only one letter can be changed at a time
* each tranformed word must exist in the wordList

Return the length of the shortest transformation sequence, or 0
if no such transformation sequence exists.

Note: beginWord does not count as a transformed word. You can
assume that beginWord and endWord are not empty and are not the same.

>>> beginWord = 'waterfall'
Word length error! 'waterfall' is larger than 5 characters. 1 <= beginWord <= 5
>>> beginWord = ''
Word length error! '' is smaller than 1 character. 1 <= beginWord <= 5
>>> beginWord = "hit"
>>> endWord = "cog"
>>> wordList = ["ABC", "dot", "dog", "log", "log", "cog"]
List error! Item in list contains entry with capitol letters
>>> wordList = ["hot", "dot", "dog", "log", "log", "cogmog"]
List error! Item in list contains entry that list longer than beginWord
>>> wordList = ["hot", "dot", "dog", "log", "log", "cog"]
>>> wordLadder(beginWord, endWord, wordList)
5
"""

class wordLadder(object):
  def __init__(self, beginWord, endWord, wordList):
    self.beginWord = beginWord
    self.endWord = endWord
    self.wordList = wordList
  def beginWord(self, word):
    if wordLength(word):
      self.beginWord = word
  def wordLength(self, word):
    # test if the word is in the valid range
    if word and len(word) in range(1,5):
      return True
    else:
      return False


