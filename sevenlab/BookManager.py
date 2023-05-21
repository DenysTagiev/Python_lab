from Book import Book
from PaperBook import  PaperBook
from ElectronicBook import ElectronicBook

class BookManager(Book):
    @staticmethod
    def main():
        books = [
            PaperBook("Father", "Maks", "Ivan", 2005, "Novel", 130, 300, 150, 200),
            PaperBook("Mum", "Denys", "Elnur", 2004, "Novel", 120, 400, 200, 250),
            ElectronicBook("Sample", "John", "ABC", 2022, "Fiction", 100, "PDF", 102400)
        ]

        for book in books:
            print