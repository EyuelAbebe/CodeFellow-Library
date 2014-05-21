
__author__ = 'eyuelabebe'


menu_options = ['A', 'B', 'C', 'a', 'b', 'c']

from constants import contentOfShelves

import sys

def _welcome(name):
    print "="*75
    print "="*22 + " Welcome to the " + name + " Library " + "="*23
    print "="*75


def _showMenu():
    main_menu = """
  You can A) Check out a book from the Library.
          B) Browse.
          C) Exit
             """
    print main_menu


def _countBookQuantity(dic, ind):
    _count = 0
    _key = dic.keys()
    if ind == 0:
        return int(dic[_key[0]]) -1
    else:
        for i in range(ind):
            _count += int(dic[_key[i]])

        return _count

def _processMenuSelection(user_selection, library):

    """
      Takes the user_selection from main menu and proceeds with corresponding options.
    """
    library = library
    if user_selection == 'A' or user_selection == 'a':

        
        library.showAvailableShelves()
        user_shelf_selection = raw_input("Choose a subject: ")

        _q  = library.showShelfBooks(list_of_shelves[int(user_shelf_selection) - 1])
        while (_q != 22):
            user_book_selection = raw_input("Choose a book: ")

            try:
                _bookdict = contentOfShelves[int(user_shelf_selection)-1][0][list_of_shelves[int(user_shelf_selection) - 1]]
                _bookindex = _countBookQuantity(_bookdict, int(user_book_selection) -1) 


                _selectedBook = books[bookObjects[int(user_shelf_selection) - 1][_bookindex].id].upper()
                bookObjects[int(user_shelf_selection) - 1][_bookindex].unshelf()
                del bookObjects[int(user_shelf_selection)-1][_bookindex]


                print "Thank you for checking out " + _selectedBook  + ". Please return on time!"
                print
            except Exception as e:
                #print books[bookObjects[int(user_shelf_selection) - 1][_bookindex].id]
                print e
                print "Sorry, we no longer have a copy of this book. Please check back again some other time."
                print
            _q = 22


        _question = raw_input("Would you like to go back to the menu(M) or exit(C): ")

        if _question not in ['C', 'c', 'm', 'M']:
            print
            print "Please select from the options presented ('C', 'M')"
            _newquestion = raw_input("Would you like to go back to the menu(M) or exit(C): ")
            if _newquestion in ['M', 'm']:
                print _showMenu()
                user_selection = raw_input(" Please make a selection: ")
                _processMenuSelection(user_selection, library)
            else:
                _processMenuSelection('C', library)
        else:
            if _question in ['C', 'c']:
                print
                print " "*20 + "Thank for using " + library.name + " Library. Do not forget to return your book on time."
                _processMenuSelection('C', library)
            if _question in ['M', 'm']:
                print _showMenu()
                user_selection = raw_input(" Please make a selection: ")
                _processMenuSelection(user_selection, library)
    


    if user_selection == 'B' or user_selection == 'b':
        library.showAllBooks()
        print _showMenu()
        _selection = raw_input("  Please make a selection:")
        _validateMenuSelection(_selection, 3, library)
        _processMenuSelection(_selection, library)

    if user_selection == 'C' or     user_selection == 'c':
        print
        print " "*20 + "******* Thank you for visiting " + library.name + " Library! GOOD DAY *******"
        sys.exit()

    _validateMenuSelection(user_selection, 3, library)


def _validateMenuSelection(user_selection, count, library):

    """
        Validates user_selection from the main menu.
    """
    counter = count

    if user_selection not in menu_options:
        if counter == 0:
            _processMenuSelection('C', library)
        else:
            print
            print "Please make your selection from the options presented!"
            user_selection = raw_input(_showMenu())
            _processMenuSelection(user_selection, library)


# ========================================================================================================================

from Library import *

smitsonian = Library()
print
_welcome(smitsonian.name)
print _showMenu()
user_selection = user_selection = raw_input(" Please make a selection: ")
_processMenuSelection(user_selection, smitsonian)

# ========================================================================================================================





