from book import Book

class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_books(self) -> list:
        return self.books

    def get_book_by_name(self, name: str) -> Book:
        for item in self.books:
            if name == item.title:
                return item
            else:
                return None

    def get_book_by_author(self, last_name: str) -> Book:
        for item in self.books:
            if last_name == item.last_name:
                return item
            else:
                return None

    def get_book_by_year(self, year: int) -> Book:
        for item in self.books:
            if year == item.year:
                return item
            else:
                return None

    def get_book_by_location(self, index: int) -> Book:
        return self.books[index]

    
