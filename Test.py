__author__ = 'eyuelabebe'


#
# from book import *
# from shelf import *
# from Library import *
# from constants import *
# from pprint import pprint
#
#
# c = Book('topology', 'math')
# d = Book('topology', 'math')
# e = Book('algebra', 'math')
# f = Book('electricity', 'physics')
# g = Book('orgo', 'chemistry')
# h = Book('inorgo', 'chemistry')
# i = Book('cells', 'biology')
# j = Book('magnetism', 'physics')
# k = Book('electricity', 'physics')
#
#
# c.enshelf()
# d.enshelf()
# e.enshelf()
# f.enshelf()
#
# g.enshelf()
# h.enshelf()
# i.enshelf()
# j.enshelf()
# k.enshelf()
#
# # math = Shelf("math")
# # math.showBooks()
#
#
# # pprint(books, width=40)
# # pprint(contentOfShelves, width=40)
# #
# # d.unshelf()
# #
# # math = Shelf("math")
# # math.showBooks()
# #
# #
# # pprint(books, width=40)
# # pprint(list_of_shelves, width=40)
# # # pprint(contentOfShelves, width=40)
# # #print c.name, c.subject, f.quantity(), j.quantity()
#
# for i in range(len(list_of_shelves)):
#     showShelfBooks(list_of_shelves[i])
#
# # showAllBooks()


from book import *
from shelf import *
from Library import *
from constants import *



Library = Library()
Library.showAllShelves()
Library.showAllBooks()
