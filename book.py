__author__ = 'eyuelabebe'

from constants import book_quantity, books, list_of_shelves, contentOfShelves, bookObjects
from random import randrange
from shelf import *


class Book():
    def __init__(self, name, subject):
        self.name = name.lower()
        self.subject = subject.lower()
        self.id = self.generateId()

        #self.enshelf()

    def generateId(self):
        bookid = randrange(len(self.name)*randrange(1000))%1000
        if bookid in books.keys():
            bookid = randrange(len(self.name)*randrange(1000))%1000

        books.update({bookid: self.name})
        self._updateQuantity()
        return bookid

    def _updateQuantity(self):
        if self.name in book_quantity.keys():
            bookqty = int(book_quantity[self.name])
            bookqty += 1
            book_quantity[self.name] = bookqty
        else:
            book_quantity.update({self.name: 1})
        #print book_quantity

    def quantity(self):
        return book_quantity[self.name]

    def enshelf(self):
        if self.subject not in list_of_shelves:
            Shelf(self.subject)
            contentOfShelves[list_of_shelves.index(self.subject)][0][self.subject].update({self.name: self.quantity()})

        else:
            contentOfShelves[list_of_shelves.index(self.subject)][0][self.subject].update({self.name: self.quantity()})

    def unshelf(self):
        _shelfContent = contentOfShelves[list_of_shelves.index(self.subject)][0]
        _title = self.name  #book_quantity.keys()[list_of_shelves.index(self.subject)]#_title = books[self.id]
        _shelfContent[self.subject][_title] += -1
        del books[self.id]



