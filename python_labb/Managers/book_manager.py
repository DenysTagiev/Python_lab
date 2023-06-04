from Exception.BookNotFoundException import BookNotFoundException
from Exception.InsufficientBooksException import InsufficientBooksException
from Exception.LoggedDecorator import LoggedDecorator
from Models.paper_book import PaperBook


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

    def __iter__(self):
        return iter(self.books)

    def display_books(self):
        for book in self.books:
            print(book)
    def get_do_something_results(self):
        return [book.do_something() for book in self.books]

    def get_enumerated_books(self):
        return list(enumerate(self.books))

    def get_zipped_results(self):
        do_something_results = [book.do_something() for book in self.books]
        return list(zip(self.books, do_something_results))

    def get_attributes_by_type(self, data_type):
        return {key: value for book in self.books for key, value in book.__dict__.items() if isinstance(value, data_type)}

    def check_conditions(self, condition):
        return {"all": all(condition(book) for book in self.books),
                "any": any(condition(book) for book in self.books)}

    def get_book_by_id(self, book_id):
        for book in self.books:
            if isinstance(book, PaperBook) and book.book_id == book_id:
                return book
        return None

    @LoggedDecorator(InsufficientBooksException, "console")
    def book(self, book_id, quantity):
        book = self.get_book_by_id(book_id)
        if book is None:
            raise BookNotFoundException("Book not found")

        if book.count_in_warehouse >= quantity:
            book.count_in_warehouse -= quantity
            return quantity
        else:
            raise InsufficientBooksException("Insufficient books available")

