CodeFellow-Library
==================

Library App for code fellow


This application consists of 3 main files, book.py, shelf.py and library.py. Each of this files designate a class for 
creating books, shelves and libraries.
Constant.py hold clobal constants that are necessary for running the application. Smithsonina.py is an applcation built using 
these 4 files.
As a user, please type entries carefully(integers or strings, when appropriate).

Inorder to start navigate to the project file and type _python Smitsonian.py_

We Create a library by naming it then adding shelves and populating shelves with books. (_NOTE: Each shelf is designated to a unique subject._)

After properly creating the library we can browse or checkout the library. See examples below:


```bash
===========================================================================
====================== Welcome to the SMITHSONINA Library =======================
===========================================================================

  You can A) Check out a book from the Library.
          B) Browse.
          C) Exit
             
None
 Please make a selection: A
-------------------------------------------------------------------
------------------------- List of Shelves -------------------------
-------------------------------------------------------------------

          1- engineering
          2- mathematics
          3- physics
          4- history

===================================================================


Choose a subject: 2

======================================================================================================================
MATHEMATICS               ID                              TITLE                                           QUANTITY
----------------------------------------------------------------------------------------------------------------------
                          1                               GEOMETRY                                        1
                          2                               CALCULS                                         1
                          3                               ALGEBRA                                         1
                          4                               TOPOLOGY                                        1
======================================================================================================================


Choose a book: 3
Thank you for checking out calculs. Please return on time!

Would you like to go back to the menu(M) or exit(D): m

  You can A) Check out a book from the Library.
          B) Browse.
          C) Exit
             
None
 Please make a selection: A
-------------------------------------------------------------------
------------------------- List of Shelves -------------------------
-------------------------------------------------------------------

          1- engineering
          2- mathematics
          3- physics
          4- history

===================================================================


Choose a subject: 2

======================================================================================================================
MATHEMATICS               ID                              TITLE                                           QUANTITY
----------------------------------------------------------------------------------------------------------------------
                          1                               GEOMETRY                                        0
                          2                               CALCULS                                         1
                          3                               ALGEBRA                                         1
                          4                               TOPOLOGY                                        1
======================================================================================================================


Choose a book: 2
Thank you for checking out calculs. Please return on time!

Would you like to go back to the menu(M) or exit(D): m

  You can A) Check out a book from the Library.
          B) Browse.
          C) Exit
             
None
 Please make a selection: A
-------------------------------------------------------------------
------------------------- List of Shelves -------------------------
-------------------------------------------------------------------

          1- engineering
          2- mathematics
          3- physics
          4- history

===================================================================


Choose a subject: 2

======================================================================================================================
MATHEMATICS               ID                              TITLE                                           QUANTITY
----------------------------------------------------------------------------------------------------------------------
                          1                               GEOMETRY                                        0
                          2                               CALCULS                                         1
                          3                               ALGEBRA                                         0
                          4                               TOPOLOGY                                        1
======================================================================================================================


Choose a book: 
Sorry, we no longer have a copy of this book. Please check back again some other time.

Would you like to go back to the menu(M) or exit(D): m

  You can A) Check out a book from the Library.
          B) Browse.
          C) Exit
             
None
 Please make a selection: B

-------------------------------------------------------------------
------------------------ List of all Books ------------------------
-------------------------------------------------------------------

          ID               TITLE
          ---------------------------

          992              ELECTRICITY
          417              TOPOLOGY
          419              SYSTEMS
          868              WORLD HISTORY
          470              LOGIC
          201              LOGIC
          941              THE AMERICAS
          176              ETHIOPIA
          916              MECHANICS
          117              MARS
          790              CALCULS
          727              MAGNETISM
          576              QUANTUM
          442              THE SUN
          957              CIRUITS
===================================================================



  You can A) Check out a book from the Library.
          B) Browse.
          C) Exit
             
None
  Please make a selection:C

                    ******* Thank you for visiting SMITHSONINA Library! GOOD DAY *******


```bash
