__author__ = 'eyuelabebe'

global list_of_shelves #Contains the subjects of books, index is shelfIdet
list_of_shelves = []

global books # key = bookId, value = book title
books = {}

global book_quantity # key = book_name, value = quantity
book_quantity = {}

global contentOfShelves # A list containing books in each shelf. Each item is a dictionary with key as book id and value another
                        # dictionary where key is number(tells same title books have same id) of tuple of book title and book quantity.
contentOfShelves = []

global bookObjects  #collection of list of book objects. Index corresponds to subject id
bookObjects = []