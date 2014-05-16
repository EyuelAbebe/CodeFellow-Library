__author__ = 'eyuelabebe'


from constants import list_of_shelves

class Shelf():

    def __init__(self, subject):
        self.subject = subject
        self.shelfNumber = self.createShelf(subject)

    def createShelf(self, subject):
        if subject.lower() in list_of_shelves:
            print "Shelf already exists. " + subject.upper() + " is shelf - " + str(list_of_shelves.index(subject))
        else:
            list_of_shelves.append(subject.lower())

            return list_of_shelves.index(subject)

    def showBooks(self):
        from constants import books


x = ['s', 'e', 's']
for i in range(len(x)):
    y = Shelf(x[i])
    print y.shelfNumber