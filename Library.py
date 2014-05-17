__author__ = 'eyuelabebe'


from constants import *
from shelf import *
from book import *

class Library():
    def __init__(self):
        self.name = raw_input("Enter name of Library: ")
        print "Lets build the " + self.name + " Library!"
        _original_number_of_shelves = raw_input("How many shelves do you want this Library to have? ")
        for i in range(int(_original_number_of_shelves)):
            _shelfSubject = raw_input("Please enter subject for shelf - " + str(i+1) + " ")
            Shelf(_shelfSubject)
            _number_of_shelf_books = raw_input("How many Books would you like to add to this shelf? ")
            for j in range(int(_number_of_shelf_books)):
                _bookTitle = raw_input("Add Title for book - " + str(j + 1) + " ")
                Book(_bookTitle, list_of_shelves[i]).enshelf()



    def showAllShelves(self):

        print
        print "*"*255
        print " "*122 + "CONTENTS OF " + self.name + " Library"
        print "*"*255
        print
        
        for i in range(len(list_of_shelves)):
            showShelfBooks(list_of_shelves[i])

    def showAllBooks(self):
        if books == {}:
            print "This is a new Library. We have no books yet."
        else:
            print "="*25
            print "ID" + " "*11 + "TITLE"
            print "-"*25
            for key, value in books.iteritems():
                print str(key) + " "*(13 - len(str(key))) + value.upper()
            print "="*25


# c = Library()
# c.showAllShelves()
# c.showAllBooks()