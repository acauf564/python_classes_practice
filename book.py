class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_data(self) -> str:
        last_name = self.author.split(" ")[1]
        first_initial = self.author.split(" ")[0][0]
        title = self.title
        year = self.year

        return f"{last_name}, {first_initial}. ({year}). {title}."