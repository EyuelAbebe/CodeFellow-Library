__author__ = 'eyuelabebe'

import sys
from constants import list_of_shelves, contentOfShelves, books

class Shelf():

    def __init__(self, subject):
        self.subject = subject.lower()
        self.createShelf()
        self.shelfNumber = getShelfNumber(self.subject)


    def createShelf(self):
        if self.subject in list_of_shelves:
            print
            print "USER ERROR: Shelf already exists. " + self.subject.upper() + " is shelf - " + str(list_of_shelves.index(self.subject) + 1)
            print "PLEASE RECREATE LIBRARY AGAIN! FOLLOW INSTRUCTIONS ACCORDINGLY. "
            print
            sys.exit()
        else:
            list_of_shelves.append(self.subject)
            self._updatecontentOfShelves()

    def _updatecontentOfShelves(self):
        contentOfShelves.append([{self.subject: {}}])


def getShelfNumber(subject):
        return list_of_shelves.index(subject)





