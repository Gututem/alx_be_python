import unittest
from io import StringIO
import sys
from library_management import Book, Library

class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        """Set up the library and books for each test."""
        self.library = Library()
        self.book1 = Book("Brave New World", "Aldous Huxley")
        self.book2 = Book("1984", "George Orwell")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertIn(self.book1, self.library._books)
        self.assertIn(self.book2, self.library._books)

    def test_check_out_book_success(self):
        msg = self.library.check_out_book("1984")
        self.assertEqual(msg, "'1984' has been checked out.")
        self.assertFalse(self.book2.is_available())

    def test_check_out_book_not_found(self):
        msg = self.library.check_out_book("Unknown Book")
        self.assertEqual(msg, "Book 'Unknown Book' not found in the library.")

    def test_return_book_success(self):
        self.library.check_out_book("1984")
        msg = self.library.return_book("1984")
        self.assertEqual(msg, "'1984' has been returned.")
        self.assertTrue(self.book2.is_available())

    def test_list_available_books(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.library.list_available_books()
        sys.stdout = sys.__stdout__

        expected_output = "Brave New World by Aldous Huxley\n1984 by George Orwell\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
