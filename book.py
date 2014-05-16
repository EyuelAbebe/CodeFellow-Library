__author__ = 'eyuelabebe'

from constants import book_quantity, books, list_of_shelves
from random import randrange


class Book():
    def __init__(self, name, subject):
        self.name = name.lower()
        self.subject = subject.lower()
        self.id = self.generateId()
        #self.quantity = self.quantity()

        #self.enshelf()

    def generateId(self):
        bookid = randrange(len(self.name)*randrange(1000))%1000
        print bookid
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
        print book_quantity


    def quantity(self):
        return book_quantity[self.name]

    def enshelf(self, subject):
        pass

    def unshelf(self):
        pass


c = Book('topology', 'math')
d = Book('topology', 'math')
e = Book('algebra', 'math')
f = Book('electricity', 'physics')



#print books
#print list_of_shelves
print c.name, c.subject, d.quantity(), c.quantity()
