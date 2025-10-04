class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return f"'{self.title}' is already checked out."
        self._is_checked_out = True
        return f"'{self.title}' has been checked out."

    def return_book(self):
        """Mark the book as returned."""
        if not self._is_checked_out:
            return f"'{self.title}' was not checked out."
        self._is_checked_out = False
        return f"'{self.title}' has been returned."

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f"Book '{title}' not found in the library."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"Book '{title}' not found in the library."

    def list_available_books(self):
        """List all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
