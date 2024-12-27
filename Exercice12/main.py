class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                break

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                break

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrow_books]


# test
library = Library()
library.add_book(Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943))
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))

library.borrow_book("1984")
print(library.available_books())
print(library.borrowed_books())
