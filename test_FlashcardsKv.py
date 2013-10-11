# -*- coding: iso-8859-1 -*-

import unittest
from StringIO import StringIO
from Flashcards import Flashcards, FlashcardsFile
from pprint import pprint

fieldnames = ['FRONTSIDE', 'BACKSIDE', 'LASTSHOWNDATE', 'NEXTSHOWDATE']

# Use german words with umlauts for tests
testfile='''"FRONTSIDE";"BACKSIDE";"LASTSHOWNDATE";"NEXTSHOWDATE"
vorderseite 1;hinterseite 1;;
Vorderseite 2;Hinterseite 2;;
Vorders�ite 3;Hinters�ite 3;;
'''

testcards=[{ 'FRONTSIDE':"vorderseite 1", 'BACKSIDE':"hinterseite 1", 'LASTSHOWNDATE':"", 'NEXTSHOWDATE':""},
        { 'FRONTSIDE':"Vorderseite 2", 'BACKSIDE':"Hinterseite 2", 'LASTSHOWNDATE':"", 'NEXTSHOWDATE':""},
        { 'FRONTSIDE':"Vorders�ite 3", 'BACKSIDE':"Hinters�ite 3", 'LASTSHOWNDATE':"", 'NEXTSHOWDATE':""}
    ]

class TestFlashcards(unittest.TestCase):
    def setUp(self):
        pass

    def test_fieldnames(self):
        fc = FlashcardsFile(StringIO(testfile)).read()
        self.assertEqual(['FRONTSIDE', 'BACKSIDE', 'LASTSHOWNDATE', 'NEXTSHOWDATE'], fc.fieldnames())

    def test_getAllCards(self):
        fc = FlashcardsFile(StringIO(testfile)).read()
        self.assertEqual(fc.getAllCards(), testcards)

if __name__ == '__main__':
    unittest.main()

