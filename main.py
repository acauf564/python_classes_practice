from bookshelf import Bookshelf
from book import Book

def read_booklist(filename: str) -> Bookshelf:
    shelf = Bookshelf()
    file = open(filename, "r")
    for line in file:
        line = line.split(",")
        shelf.add_book(Book(line[0], line[1], int(line[2])))

    return shelf

def main():
    # bookshelf = Bookshelf()
    # bookshelf.add_book(Book("No Longer Human", "Osamu Dazai", 1948))
    # bookshelf.add_book(Book("The Parallax View", "Slavoj Žižek", 2006))
    # bookshelf.add_book(Book("Fear Stalks the Land!", "Thom Yorke", 2021))

    # for item in bookshelf.get_books():
    #     print(item.get_data())

    matts_list = read_booklist("my_shelf.txt")

    for item in matts_list.get_books():
        print(item.get_data())

main()
