## Adding Files Hints

<details>
    <summary>Adding one book</summary>

```py
    def main():
    bookshelf = Bookshelf()

    no_longer_human = Book("No Longer Human", "Osamu Dazai", 1948)

    bookshelf.add_book(no_longer_human)
```

</details>
<br />

## Adding Files Solution

<details>
    <summary>Adding ALL the books</summary>

```py
    def main():
    bookshelf = Bookshelf()

    no_longer_human = Book("No Longer Human", "Osamu Dazai", 1948)
    the_parallax_view = Book("No Longer Human", "Slavoj Žižek", 2006)
    fear_stalks = Book("Fear Stalks the Land!", "Thom Yorke", 2021)

    bookshelf.add_book(no_longer_human)
    bookshelf.add_book(the_parallax_view)
    bookshelf.add_book(fear_stalks)
```

</details>

<details>
    <summary>Adding books in less lines</summary>

Really, you don't _have_ to set a variable per book, you can just create the book and add it to the shelf in one line, like this:

```py
def main():
    bookshelf = Bookshelf()

    bookshelf.add_book(Book("No Longer Human", "Osamu Dazai", 1948))
    bookshelf.add_book(Book("No Longer Human", "Slavoj Žižek", 2006))
    bookshelf.add_book(Book("Fear Stalks the Land!", "Thom Yorke", 2021))
```
