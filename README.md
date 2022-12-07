# Bookshelf Practice Problem

You're given two classes, `Bookshelf` and `Book`.

`Book`s have a few properties: a `title`, an `author`, and a `year of publication`.

A `Bookshelf` only has one property: a `books` list.

## Adding some books

In your code, please manually create the following books, and add them to a bookshelf.

| Book Title            | Author          | Year |
| --------------------- | --------------- | ---- |
| No Longer Human       | Osamu Dazai     | 1948 |
| The Parallax View     | Slavoj Žižek    | 2006 |
| Fear Stalks the Land! | Thom Yorke      | 2021 |
| A Certain Hunger      | Chelsea Summers | 2020 |
| The Stranger          | Albert Camus    | 1942 |

## Those better be right...

These are some of my favourite books, so you better make sure they're all correct.
Create a _method_ in the `Book` class called `get_data()` to return the book's information. I really like APA, so format it like this:

```
Dazai, O. (1948). No Longer Human.
```

Now, loop through every book on the shelf and print out its data.

## Find me a book!

Time for some `Bookshelf` methods! I'm gonna need three of 'em:

### By title

Pretty self explanitory, make a method called `get_book_by_name()` that takes a string `name`, and returns the `Book` with the same title! If it's not on the shelf, just return `None`.

### By author name

This is a little trickier, make a method called `get_book_by_author()` that takes a string `last_name` (not first name), and returns the `Book` written by them! Don't worry, there's only one book per author (so far...). If there isn't a book written by them, don't worry, just return `None`.

### By date of publication

You don't need a hint for this one, do you?

### By location on shelf

Maybe I want the first book on my shelf, can you get that for me?
I don't want the `0th` book, I don't know what that is. I want the **first** thing!

## More books!!

I've included a file called `my_shelf.txt` in this repo. In it is a bunch of books, their authors, and their publication dates. Read these and turn them into `Book`s please. Oh, and put them on a `Bookshelf`.
