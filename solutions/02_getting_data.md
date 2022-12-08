## Getting data hints

<details>
    <summary>Formatting</summary>

There's a lot of data we're gonna need to print out, and the best way to do it with with an **fstring**!

```py
    website = "fstring.help"
    print(f"Go to this website for some hints: {fstring.help}")
```

</details>

<details>
    <summary>Getting our data ready</summary>

Well, let's think about what data we need: The `last_name`, the `first_initial`, the `title`, and the `year` of publication. Let's put these into some variables:

```py
    last_name = self.author.split(" ")[?]
    first_initial = self.author.split(" ")[?][?]
    title = self.title
    year = self.year
```

I'm not gonna give you the indexes just yet, you can do those yourselves.

</details>
<br />

## Getting Data Solution

<details>
    <summary>*actually* formatting</summary>

```py
    class Book:
        def __init__(self, title: str, author: str, year: int):
            self.title = title
            self.author = author
            self.year = year

        def get_data(self): # remember the self argument!
            last_name = self.author.split(" ")[1] # let's split this up into first name last name, and grab the last name.
            first_initial = self.author.split(" ")[0][0] # let's grab the first initial!
            title = self.title
            year = self.year

            return f"{last_name}, {first_initial} ({year}). {title}."

```
