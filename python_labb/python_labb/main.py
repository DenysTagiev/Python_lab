from Managers.book_manager import BookManager

from Models.electronic_book import ElectronicBook

from Models.paper_book import PaperBook
from Models.electronic_book import ElectronicBook
from Managers.book_manager import BookManager


def main():
    paper_book = PaperBook("Father", "Maks", "Ivan", 2005, "Novel", 130, 300, 150)
    electronic_book = ElectronicBook("Sample", "John", "ABC", 2022, "Fiction", 100, 200, "PDF", 1920)

    book_manager = BookManager()
    book_manager.add_book(paper_book)
    book_manager.add_book(electronic_book)

    do_something_results = book_manager.get_do_something_results()
    print("Results of do_something():", do_something_results)

    enumerated_books = book_manager.get_enumerated_books()
    print("Enumerated books:", enumerated_books)

    zipped_results = book_manager.get_zipped_results()
    print("Zipped results:", zipped_results)

    attributes = book_manager.get_attributes_by_type(int)
    print("Attributes with int values:", attributes)

    bool_conditions = book_manager.check_conditions(lambda book: book.pages > 100)
    print("Conditions check:", bool_conditions)

    book_manager.display_books()


if __name__ == "__main__":
    main()
