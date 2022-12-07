from book import Book


class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
