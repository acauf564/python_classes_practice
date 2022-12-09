# Bookshelf Practice Problem

You're given two classes, `Bookshelf` and `Book`.

`Book`s have a few properties: a `title`, an `author`, and a `year of publication`. We set these when **instantiating** the book.

A `Bookshelf` only has one property: a `books` list. It's empty by default.

## Adding some books

In your code, please manually create the following books, and add them to a bookshelf.

| Book Title            | Author       | Year |
| --------------------- | ------------ | ---- |
| No Longer Human       | Osamu Dazai  | 1948 |
| The Parallax View     | Slavoj Žižek | 2006 |
| Fear Stalks the Land! | Thom Yorke   | 2021 |

## Those better be right...

These are some of my favourite books, so you better make sure they're all correct.
Create a _method_ in the `Book` class called `get_data()` to return the book's information. I really like APA, so format it like this:

```
Dazai, O. (1948). No Longer Human.
```

Now, loop through every book on the shelf and print out its data.

A quick hint for the last name first initial thing: we may want to **split** our name into two parts. This will let us pick out our first name and our last name and do what we need with them.

## Find me a book!

Time for some `Bookshelf` methods! I'm gonna need a few of 'em:

### By title

Pretty self explanitory, make a method called `get_book_by_name()` that takes a string `name`, and returns the `Book` with the same title! If it's not on the shelf, just return `None`.

### By author name

This is a little trickier, make a method called `get_book_by_author()` that takes a string `last_name` (not first name), and returns the `Book` written by them! Don't worry, there's only one book per author (so far...). If there isn't a book written by them, don't worry, just return `None`.

### By date of publication

You don't need a hint for this one, do you?

### By location on shelf

Maybe I want the first book on my shelf, can you get that for me?
I don't want the `0th` book, I don't know what that is. I want the **first** thing! This can be a one line function by the way.

## More books!!

I've included a file called `my_shelf.txt` in this repo. In it is a bunch of books, their authors, and their publication dates. Read these and turn them into `Book`s please. Oh, and put them on a `Bookshelf`. You shouldn't _have_ to `try/except` these, but if you want to, be my guest. It ain't gonna be on the exam, so I don't care too much.

Also, you're gonna need to make some edits to some existing functions. Not all these authors have a last name, so you're just gonna have to use their first name without an initial.

Also, a few of those methods up there need to be edited. There are gonna be a few books that were written in the same year, or by the same author. Just return a list full of them. If there's only one book that matches the criteria, just return the one book in a list.

## More methods!!!

Now, I've included a lot of books. This is a real depiction of my shelf at home. Literally, I've read all\* of these. Don't judge. Now, let's do some sorting.

###### \*edit: My girlfriend would like to inform you that I am a liar and have **not** read all of these.

### I'm old at heart

I've got a lot of classics on my shelf. Dostoevsky, Camus, Orwell, Huxley, you name it, I've got it. Write me a method where I can specify a `year`, and it returns a list of books, all writen **before or during that year**.

### Duplicate authors

There are a few authors I really like, and I own a couple books for each of them. Write a method that returns a list of the names of the authors that I have **more than one** book of. Full names, please.

### Duplicate book

I've got two copies of the same book on my shelf! One's really old, and one's a new version. Could you write a method to find what book I have two of, and **remove** the old version from my shelf?

## A Trip to IKEA

Time for a new shelf. Could you take all the books written by an author with a last name between **A and K** and move them into the new shelf. You can delete them from the old shelf when you're done.

## Moving Out

I've got to pack up these books and move them to a new apartment. Can you create a `MovingBox` class that stores its own list of `books`? Also, books are heavy, so make sure that when I `add_book()` to this box, that I don't have over `15` books. Make as many boxes as you need, and put 'em into a list for me. I'll unpack those later.
