#Library Management System
Python script uses Tkinter for the graphical user interface (GUI) and MySQL for the backend database to create a basic Library Management System. It begins by defining functions to connect to the MySQL database (connect_db()), fetch and display all books (view_books()), edit a selected book (edit_book()), update book details (update_book()), and add a new book (add_book()).

The GUI is set up using Tkinter, with the main window titled "Library Management System" (root). Entry fields and labels for book details (title, author, ISBN, quantity) are provided, along with buttons to add a book (Add Book) and view all books (View All Books).

When a user adds a book, the add_book() function retrieves input values from the entry fields and inserts them into the MySQL database table books. Upon successful addition, a message box confirms the operation.

The view_books() function retrieves all books from the database and displays them in a new window (view_books_window). Each book is shown in a row with an "Edit" button that opens the edit_book() function, allowing users to modify book details.

The edit_book() function opens a new window (edit_window) pre-filled with the current book details for editing. The update_book() function updates the edited book details in the database and closes the edit window upon successful update, displaying a success message.

Overall, this script provides essential functionalities for managing a library collection through a user-friendly GUI, facilitating book additions, edits, and view operations seamlessly integrated with a MySQL database backend.
