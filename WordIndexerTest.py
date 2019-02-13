import unittest
from WordIndexer import WordIndexer
import os

class WordIndexerTest(unittest.TestCase):


    def runTest(self):
        wordIndexer = WordIndexer('files/comedy-of-errors.txt')
        wordIndexer.extract().generate()
        self.assertTrue(os.path.exists('files/comedy-of-errors-index.txt'))
        os.remove('files/comedy-of-errors-index.txt')