
__author__ = 'eyuelabebe'


menu_options = ['A', 'B', 'C', 'D']
wrong_menu_options = ['a', 'b', 'c', 'd']


import sys

def _welcome(name):
    print "="*75
    print "="*22 + " Welcome to the " + name + " Library " + "="*23
    print "="*75


def _showMenu():
    main_menu = """
  You can A) Check out a book from the Library.
          B) Return a book.
          C) Browse.
          D) Exit

  Please make a selection:
             """
    print main_menu


def _processMenuSelection(user_selection, library):

    """
      Takes the user_selection from main menu and proceeds with corresponding options.
    """
    library = library
    if user_selection == 'A':

        try:
            library.showAvailableShelves()
            user_shelf_selection = raw_input("Choose a subject: ")

            library.showShelfBooks(list_of_shelves[int(user_shelf_selection) - 1])
            user_book_selection = raw_input("Choose a book: ")
            try:
                print books
                print
                print bookObjects
                bookObjects[int(user_shelf_selection) - 1][int(user_book_selection)-1].unshelf()
                print books
                print
                bookObjects[int(user_shelf_selection)-1].pop(int(user_book_selection)-1)
                print bookObjects
                print "Thank you for checking out " + books[bookObjects[int(user_shelf_selection) - 1][int(user_book_selection)-1].id] + ". Please return on time!"
                print
            except Exception as e:
                print e
                print "Sorry, we no longer have a copy of this book. Please check back again some other time."
                print

            _question = raw_input("Would you like to go back to the menu(M) or exit(D)")

            if _question not in ['d', 'D', 'm', 'M']:
                print
                print "Please select from the options presented ('D', 'M')"
                _newquestion = raw_input("Would you like to go back to the menu(M) or exit(D): ")
                if _newquestion in ['M', 'm']:
                    user_selection = raw_input(_showMenu())
                    _processMenuSelection(user_selection, library)
                else:
                    _processMenuSelection('D', library)
            else:
                if _question in ['D', 'd']:
                    print
                    print " "*20 + "Thank for using " + library.name + " Library. Do not forget to return your book on time."
                    _processMenuSelection('D', library)
                if _question in ['M', 'm']:
                    user_selection = raw_input(_showMenu())
                    _processMenuSelection(user_selection, library)
        except:
            print
            print "USER ERROR: ENTERED WRONG SELECTION. GOOD BYE!"




        ##book_id_selection = raw_input( "Choose a book id from the list")
        ##print main_menu

        #book_selection = raw_input("")
    if user_selection == 'B':
        _processMenuSelection('D')


    if user_selection == 'C':
        library.showAllBooks()
        _selection = runMenu(library)
        _processMenuSelection(_selection, library)

    if user_selection == 'D':
        print
        print " "*20 + "******* Thank you for visiting " + library.name + " Library! GOOD DAY *******"
        sys.exit()

    _validateMenuSelection(user_selection, 3, library)


def _validateMenuSelection(user_selection, count, library):

    """
        Validates user_selection from the main menu.
    """
    counter = count

    if user_selection in wrong_menu_options:
        if counter == 0:
            _processMenuSelection("D", library)
        else:
            counter += -1
            print
            print "Please use capital letters."
            user_selection = raw_input(_showMenu())
            _validateMenuSelection(user_selection, counter)

    if user_selection not in menu_options:
        if counter == 0:
            _processMenuSelection('D', library)
        else:
            print
            print "Please make your selection from the options presented!"
            user_selection = raw_input(_showMenu())
            _processMenuSelection(user_selection, library)


def runMenu(library):
    user_selection = raw_input(_showMenu())
    _validateMenuSelection(user_selection, 3, library)
    return user_selection


# ========================================================================================================================

from Library import *
from constants import *

smitsonian = Library()
_welcome(smitsonian.name)
user_selection = raw_input(_showMenu())
_processMenuSelection(user_selection, smitsonian)

# ========================================================================================================================





