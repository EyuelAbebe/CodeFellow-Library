__author__ = 'eyuelabebe'


from constants import *
from shelf import *
from book import *
import sys

class Library():
    def __init__(self):
        self.name = raw_input("Enter name of Library: ").upper()
        print
        print "-"*(4) + " Lets build the " + self.name.upper() + " Library " + "-"*(4)
        print
        print
        _original_number_of_shelves = raw_input("How many shelves do you want this Library to have? ")
        print

        try:
            for i in range(int(_original_number_of_shelves)):
                _list_of_subject_books = []
                print
                _shelfSubject = raw_input("Please enter subject for shelf - " + str(i+1) + " ")
                Shelf(_shelfSubject)
                print
                _number_of_shelf_books = raw_input("How many Books would you like to add to this shelf? ")
                try:
                    for j in range(int(_number_of_shelf_books)):
                        _bookTitle = raw_input("Add Title for book - " + str(j + 1) + " ")
                        _book = Book(_bookTitle, list_of_shelves[i])
                        _book.enshelf()
                        _list_of_subject_books.append(_book)
                except ValueError:
                    print
                    print "USER ERROR: Entered a string instead of an Integer "
                    print " "*10 + "-"*(4) + "GOOD BYE" + "-"*(4)
                    print
                    sys.exit()

                bookObjects.append(_list_of_subject_books)

        except ValueError:
            print
            print "USER ERROR: Entered a string instead of an Integer "
            print " "*10 + "-"*(4) + " GOOD BYE " + "-"*(4)
            sys.exit()


    def showAllBooks(self):
        if books == {}:
            print
            print "This is a new Library. We have no books yet."
        else:
            print
            print "-"*67
            print "-"*24 + " List of all Books " + "-"*24
            print "-"*67
            print

            print " "*10 + "ID" + " "*15 + "TITLE"
            print " "* 10 + "-"*27
            print
            for key, value in books.iteritems():
                print " "*10 + str(key) + " "*(15 - len(str(key)) + 2) + value.upper()
            print "="*67
            print
            print

    def showShelfBooks(self, subject):
        _shelf = contentOfShelves[getShelfNumber(subject)][0][subject]
        _spacer = 15#len(subject)

        print
        print "=" * (_spacer *7 + 13)
        print subject.upper()  + " "*(_spacer)+ "ID" + " " * (_spacer*2) + "TITLE" + " " * (_spacer *3 - 2) + "QUANTITY"
        print "-" * (_spacer *7 + 13)

        if _shelf.keys() == []:
            print
            print "Shelf is Empty!"
        else:
            _i = 1
            for key in _shelf:

                print  " "*(_spacer + len(subject)) + str(_i) + " " * (_spacer *2 + 2 - len(str(_i)) ) + key.upper() + " " * ((_spacer *3 ) - len(key) ) + "   " + str(_shelf[key])
                _i += 1
        print "=" * (_spacer *7 + 13)
        print
        print


    def showAllShelves(self):
        print
        print "*"*180
        print " "*(80 - len(self.name)) + "CONTENTS OF " + self.name + " Library"
        print "*"*180
        print
        print

        for i in range(len(list_of_shelves)):
            self.showShelfBooks(list_of_shelves[i])

    def showAvailableShelves(self):
        print "-"*67
        print "-"*25 + " List of Shelves " + "-"*25
        print "-"*67
        print
        for i in range(len(list_of_shelves)):
            print " "*10 + str(i + 1) + "- " + list_of_shelves[i]
        print
        print "="*67
        print
        print

