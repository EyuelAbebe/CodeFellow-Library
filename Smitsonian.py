

from constants import *
import sys


def openLibrary():

    """
        Welcome page and user selection.
    """
    print welcome
    user_selection = raw_input(main_menu)
    processSubjectSelection(user_selection)


def showSubjects():

    """
        Lists out all the that are subjects available.
    """

    print subjectChoices


def selectSubject():

    """
        Shows subject choice then returns a users subject choice.
    """
    showSubjects()
    user_selection = raw_input(selection)
    validateSubjectSelection(user_selection, 3)

    return user_selection


def showBooks(subject):

    """
        Lists out all the books available in the given subject.
    """

    print "============================================================"
    print "-- " + subjects[subject]
    print " "
    print " Id              Books"
    print "====           ======== "
    for key, value in book[subject].items():
        print str(key) + "          " + str(value)

    print " "

def validateSubjectSelection(user_selection, count):

    """
        Validates if the user's subject selection is correct.
    """

    counter = count

    if counter == 0:
        processSubjectSelection("E")

    if (user_selection not in subject_options):
        return True
    else:
        counter += -1
        print " "
        print "Please pick from the options presented"
        user_selection = raw_input(showSubjects())
        validateSubjectSelection(user_selection, counter)


def validateMenuSelection(user_selection, count):

    """
        Validates user_selection from the main menu.
    """
    counter = count

    if user_selection in wrong_menu_options:
        if counter == 0:
            processSelection("E")
        else:
            counter += -1
            print "Please use capital letters."
            user_selection = raw_input(main_menu)
            validateMenuSelection(user_selection, counter)

    if user_selection not in menu_options:
        if counter == 0:
            processSubjectSelection('E')
        else:
            print "Please make your selection from the options presented!"
            user_selection = raw_input(main_menu)
            processSubjectSelection(user_selection)


def processSubjectSelection(user_selection):

    """
      Takes the user_selection from main menu and proceeds with corresponding options.
    """

    if user_selection == 'A':
        user_subject_selection = int(selectSubject())
        showBooks(user_subject_selection)

        ##book_id_selection = raw_input( "Choose a book id from the list")
        ##print main_menu

        #book_selection = raw_input("")

    if user_selection == 'B': processSubjectSelection('E')
    if user_selection == 'C': processSubjectSelection('E')
    if user_selection == 'D': processSubjectSelection('E')
    if user_selection == 'E':
        print "******* Thank you for visiting Smithsonian Library! GOOD DAY *******"
        sys.exit()

    validateMenuSelection(user_selection, 3)




openLibrary()









