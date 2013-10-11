# -*- coding: iso-8859-1 -*-

# Informationen zum Encoding von Strings und Dateien: http://wiki.python.de/Von%20Umlauten,%20Unicode%20und%20Encodings, gute Infos zu Unicode.

import csv
import sys

class Flashcards:
    __iterator = 0

    def __init__(self, fieldnames, rows):
        self.__fieldnames = fieldnames
        self.__rows = []
        for row in rows:
            self.__rows.append(row)
        self.__rows_to_export = set(range(0, len(self.__rows)))
        self.__fsencoding = sys.getfilesystemencoding()

    def fieldnames(self):
        """ Liefert eine Liste mit den Feldnamen, wie sie von PmExportFile aus der Datei gelesen wird. Feldnamen = erste Reihe in der Datei.
        """
        return self.__fieldnames

    def getAllCards(self):
        return self.__rows

    def toFirstCard(self):
        self.__iterator = 0

    def nextCard(self):
        if self.__iterator < len(self.__rows)-1:
            self.__iterator = self.__iterator + 1
        else:
            self.__iterator = 0

    def front(self):
        return self.__rows[self.__iterator]['FRONTSIDE']

    def back(self):
        return self.__rows[self.__iterator]['BACKSIDE']


class FlashcardsFile:
    def __init__(self, file):
        """ Takes a file (returned by open(...)) and returns a Flashcards object.
        """
        self.__file = file
        
    def read(self):
        """ Reads the cvs file. The default delimiter is a semicolon (;).
        """
        self.__addrReader = csv.DictReader(self.__file, delimiter=';', restkey='UnknownFields')
        return Flashcards(self.__addrReader.fieldnames, [row for row in self.__addrReader])

    def write(self, pmexport):
        """ Writes a cvs file. The default delimiter is a semicolon (;).
        """
        self.__addrWriter = csv.DictWriter(self.__file, pmexport.fieldnames(), delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        self.__addrWriter.writeheader()
        self.__addrWriter.writerows(pmexport.rows())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="A Python class for reading flashcard (Leitner-System) from csv files.")
    parser.add_argument("--dump", action="store", nargs='+', help="Excludes lines matching an element from the exclude list.")
    args = parser.parse_args()


