
__author__ = 'eyuelabebe'


menu_options = ['A', 'B', 'C']
wrong_menu_options = ['a', 'b', 'c']


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

                bookObjects[int(user_shelf_selection) - 1][int(user_book_selection)-1].unshelf()
                bookObjects[int(user_shelf_selection)-1].pop(int(user_book_selection)-1)
                print "Thank you for checking out " + books[bookObjects[int(user_shelf_selection) - 1][int(user_book_selection)-1].id] + ". Please return on time!"
                print
            except Exception as e:
                #print e
                print "Sorry, we no longer have a copy of this book. Please check back again some other time."
                print

            _question = raw_input("Would you like to go back to the menu(M) or exit(D): ")

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
        except:
            print
            print "USER ERROR: ENTERED WRONG SELECTION. GOOD BYE!"
            sys.exit()


    if user_selection == 'B':
        library.showAllBooks()
        print _showMenu()
        _selection = raw_input("  Please make a selection:")
        _validateMenuSelection(_selection, 3, library)
        _processMenuSelection(_selection, library)

    if user_selection == 'C':
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
            _processMenuSelection("C", library)
        else:
            counter += -1
            print
            print "Please use capital letters."
            user_selection = raw_input(_showMenu())
            _validateMenuSelection(user_selection, counter, library)

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
_welcome(smitsonian.name)
print _showMenu()
user_selection = user_selection = raw_input(" Please make a selection: ")
_processMenuSelection(user_selection, smitsonian)

# ========================================================================================================================





