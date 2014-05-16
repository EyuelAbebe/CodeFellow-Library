__author__ = 'eyuelabebe'

from book import *
from shelf import *
from constants import *

def getShelfNumber(subject):
        return list_of_shelves.index(subject)

def showShelfBooks(subject):
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


def showAllBooks():
    if books == {}:
        print "This is a new Libarry. We have no books yet."
    else:
        print "="*25
        print "ID" + " "*11 + "TITLE"
        print "-"*25
        for key, value in books.iteritems():
            print str(key) + " "*(13 - len(str(key))) + value.upper()
        print "="*25



#================================================= TEST =================================================
from pprint import pprint


c = Book('topology', 'math')
d = Book('topology', 'math')
e = Book('algebra', 'math')
f = Book('electricity', 'physics')
g = Book('orgo', 'chemistry')
h = Book('inorgo', 'chemistry')
i = Book('cells', 'biology')
j = Book('magnetism', 'physics')
k = Book('electricity', 'physics')


c.enshelf()
d.enshelf()
e.enshelf()
f.enshelf()

g.enshelf()
h.enshelf()
i.enshelf()
j.enshelf()
k.enshelf()

# math = Shelf("math")
# math.showBooks()


# pprint(books, width=40)
# pprint(contentOfShelves, width=40)
#
# d.unshelf()
#
# math = Shelf("math")
# math.showBooks()
#
#
# pprint(books, width=40)
# pprint(list_of_shelves, width=40)
# # pprint(contentOfShelves, width=40)
# #print c.name, c.subject, f.quantity(), j.quantity()

for i in range(len(list_of_shelves)):
    showBooks(list_of_shelves[i])

showAllBooks()