import tkinter as tk
from tkinter import messagebox, simpledialog
import mysql.connector

# Function to connect to MySQL database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="devnaina",
            database="library_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to fetch and display all books
def view_books():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "SELECT id, title, author, isbn, quantity FROM books"
        cursor.execute(query)
        books = cursor.fetchall()
        conn.close()

        # Create a new window to display books
        view_books_window = tk.Toplevel(root)
        view_books_window.title("View All Books")

        # Create a table to display books
        tk.Label(view_books_window, text="ID",borderwidth=3, bg="black",fg="lavender",font=("bold")).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(view_books_window, text="Title",borderwidth=3, bg="black",fg="lavender",font=("bold")).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(view_books_window, text="Author",borderwidth=3, bg="black",fg="lavender",font=("bold")).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(view_books_window, text="ISBN",borderwidth=3, bg="black",fg="lavender",font=("bold")).grid(row=0, column=3, padx=5, pady=5)
        tk.Label(view_books_window, text="Quantity",borderwidth=3, bg="black",fg="lavender",font=("bold")).grid(row=0, column=4, padx=5, pady=5)
        tk.Label(view_books_window, text="Action",borderwidth=3, bg="black",fg="lavender",font=("bold")).grid(row=0, column=5, padx=5, pady=5)

        # Display each book in a row with an edit button
        for i, book in enumerate(books, start=1):
            tk.Label(view_books_window, text=book[0]).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(view_books_window, text=book[1]).grid(row=i, column=1, padx=5, pady=5)
            tk.Label(view_books_window, text=book[2]).grid(row=i, column=2, padx=5, pady=5)
            tk.Label(view_books_window, text=book[3]).grid(row=i, column=3, padx=5, pady=5)
            tk.Label(view_books_window, text=book[4]).grid(row=i, column=4, padx=5, pady=5)
            edit_button = tk.Button(view_books_window, text="Edit",font=("Helvetica",15,"bold"), command=lambda b=book: edit_book(b))
            edit_button.grid(row=i, column=5, padx=5, pady=5)

# Function to edit a selected book
def edit_book(book):
    # Create a dialog window to edit book details
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Book")

    tk.Label(edit_window, text="Title:",font=("Helvetica",15,"bold")).grid(row=0, column=0, padx=10, pady=5)
    title_entry = tk.Entry(edit_window,borderwidth=3, bg="black",fg="lavender")
    title_entry.grid(row=0, column=1, padx=10, pady=5)
    title_entry.insert(0, book[1])

    tk.Label(edit_window, text="Author:",font=("Helvetica",15,"bold")).grid(row=1, column=0, padx=10, pady=5)
    author_entry = tk.Entry(edit_window,borderwidth=3, bg="black",fg="lavender")
    author_entry.grid(row=1, column=1, padx=10, pady=5)
    author_entry.insert(0, book[2])

    tk.Label(edit_window, text="ISBN:",font=("Helvetica",15,"bold")).grid(row=2, column=0, padx=10, pady=5)
    isbn_entry = tk.Entry(edit_window,borderwidth=3, bg="black",fg="lavender")
    isbn_entry.grid(row=2, column=1, padx=10, pady=5)
    isbn_entry.insert(0, book[3])

    tk.Label(edit_window, text="Quantity:",font=("Helvetica",15,"bold")).grid(row=3, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(edit_window,borderwidth=3, bg="black",fg="lavender")
    quantity_entry.grid(row=3, column=1, padx=10, pady=5)
    quantity_entry.insert(0, book[4])

    update_button = tk.Button(edit_window, text="Update",font=("Helvetica",15,"bold"), command=lambda: update_book(book[0], title_entry.get(), author_entry.get(), isbn_entry.get(), quantity_entry.get(), edit_window))
    update_button.grid(row=4, column=0, columnspan=2, pady=10)

# Function to update book details in the database
def update_book(book_id, title, author, isbn, quantity, window):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE books SET title=%s, author=%s, isbn=%s, quantity=%s WHERE id=%s"
        data = (title, author, isbn, quantity, book_id)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book updated successfully!")
        window.destroy()  # Close the edit window after updating

# Function to add a book to the database
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    quantity = quantity_entry.get()

    if not title or not author or not isbn or not quantity:
        messagebox.showerror("INPUT ERROR","All the fields are mandatory")
    
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO books (title, author, isbn, quantity) VALUES (%s, %s, %s, %s)"
        data = (title, author, isbn, quantity)
        cursor.execute(query, data)
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")
        conn.close()

# GUI Setup using Tkinter
root = tk.Tk()
root.title("Library Management System")

# Labels and Entry boxes for adding a book
tk.Label(root, text="Title:",font=("Helvetica",15,"bold")).grid(row=0, column=0, padx=10, pady=5)
title_entry = tk.Entry(root,borderwidth=3, bg="black",fg="lavender")
title_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Author:",font=("Helvetica",15,"bold")).grid(row=1, column=0, padx=10, pady=5)
author_entry = tk.Entry(root,borderwidth=3, bg="black",fg="lavender")
author_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="ISBN:",font=("Helvetica",15,"bold")).grid(row=2, column=0, padx=10, pady=5)
isbn_entry = tk.Entry(root,borderwidth=3, bg="black",fg="lavender")
isbn_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Quantity:",font=("Helvetica",15,"bold")).grid(row=3, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(root,borderwidth=3, bg="black",fg="lavender")
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

# Button to add a book
add_book_button = tk.Button(root, text="Add Book", command=add_book,font=("Helvetica",15,"bold"))
add_book_button.grid(row=4, column=0, columnspan=2, pady=10)

# Button to view all books
view_books_button = tk.Button(root, text="View All Books", command=view_books,font=("Helvetica",15,"bold"))
view_books_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
