__author__ = 'eyuelabebe'


from constants import list_of_shelves, contentOfShelves

class Shelf():

    def __init__(self, subject):
        self.subject = subject.lower()
        self.createShelf()
        self.shelfNumber = getShelfNumber(self.subject)


    def createShelf(self):
        if self.subject in list_of_shelves:
            print "Shelf already exists. " + self.subject.upper() + " is shelf - " + str(list_of_shelves.index(self.subject))
        else:
            list_of_shelves.append(self.subject)
            self._updatecontentOfShelves()

    def _updatecontentOfShelves(self):
        contentOfShelves.append([{self.subject: {}}])

def getShelfNumber(subject):
        return list_of_shelves.index(subject)


def showBooks(subject):
    _shelf = contentOfShelves[getShelfNumber(subject)][0][subject]
    _spacer = len(subject)

    print "=" * (_spacer *7 + 9)
    print subject.upper() + " " * (_spacer ) + "ID" + " " * (_spacer*2 - 2) + "TITLE" + " " *(_spacer *3 -5 ) + "QUANTITY"
    print "-" * (_spacer *7 + 9)

    if _shelf.keys() == []:
        print "Shelf is Empty!"
    else:
        for key in _shelf:
            print " " * (_spacer *2) + "000" + " " * ((_spacer *2) - 3) + key.upper() + " " * ((_spacer *3) - len(key)) + str(_shelf[key])

    print "=" * (_spacer *7 + 9)
    print
    print
    print




