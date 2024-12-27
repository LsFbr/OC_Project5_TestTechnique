class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    # Initialisation des attributs
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Méthode pour ajouter un livre à la bibliothèque
    def add_book(self, book):
        self.books.append(book)

    # Méthode pour supprimer un livre de la bibliothèque
    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break

    # Méthode pour emprunter un livre
    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                break

    # Méthode pour rendre un livre
    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                break

    # Méthode pour afficher les livres disponibles
    def available_books(self):
        return [book.title for book in self.books]

    # Méthode pour afficher les livres empruntés
    def borrowed_books(self):
        return [book.title for book in self.borrow_books]


# Test
library = Library()
library.add_book(Book("Harry Potter", "J.K. Rowling", 1997))
library.add_book(Book("The Lord of the Rings", "J.R.R. Tolkien", 1954))
library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 1937))

library.borrow_book("The Lord of the Rings")
print(library.available_books())
print(library.borrowed_books())
