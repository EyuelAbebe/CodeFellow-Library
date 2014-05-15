welcome = """ 
==================== Welcome to the Smithsonina Library ====================
"""

subjectChoices = """  We have books in the following subjects:
          0 Mathematics
          1 Physics
          2 Chemistry
          3 Biology
          4 Engineering

"""

main_menu = """
  You can A) Check out a book from the Library.
          B) Return a book.
          C) Donate a book.
          D) Browse
          E) Exit

  Please make a selection: """

selection = " Please pick an option: "

menu_options = ['A', 'B', 'C', 'D', 'E']
wrong_menu_options = ['a', 'b', 'c', 'd', 'e']

global book
book = [{0001: "Differential Geometery",
         0002: "Analytical Calculus",
         0003: "Topology"},
        {1001: "Electricity and Magnetism",
         1002: "Classical Mechanics"},
        {2001: "Organic Chemistry",
         2002: "Inorganic Chemistry"},
        {3001: "Human Anatomy",
         3002: "Reproductive Biology",
         3003: "Cells"},
        {4001: "Statics",
         4002: "Circuits and Systems",
         4003: "Embeded systems",
         4004: "Analogy Design",
         4005: "Foundations of Computer Science",
         4006: "Software Engineering"}
        ]

global books
books = {'A': 0,
         'B': 1,
         'C': 2,
         'D': 3,
         'E': 4}

global subjects
subjects = {0: 'Mathematics',
            1: 'Physics',
            2: 'Chemistry',
            3: 'Biology',
            4: 'Engineering'}

global subject_options
subject_options = subjects.keys()

book_id = [0001, 0002, 0003, 1001, 1002, 2001, 2002, 3001, 3002, 3003, 4001, 4002, 4003, 4004, 4005, 4006]
