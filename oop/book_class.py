class Book:
    def __init__(self, title, author, year):
        """Constructor that initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that announces deletion of the object."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an unambiguous representation that can recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
