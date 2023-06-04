from Models.Book import Book

class ElectronicBook(Book):
    def __init__(self, title="", author="", publisher="", year=0, genre="", count_in_warehouse=0, pages=0, format="", file_size_in_bytes=0):
        super().__init__(title, author, publisher, year, genre)
        self.count_in_warehouse = count_in_warehouse
        self.pages = int(pages)
        self.format = format
        self.file_size_in_bytes = file_size_in_bytes


    def book(self, quantity):
        if self.count_in_warehouse >= quantity:
            self.count_in_warehouse -= quantity
            return quantity
        else:
            available_books = self.count_in_warehouse
            self.count_in_warehouse = 0
            return available_books

    def has_more_books(self):
        return self.count_in_warehouse > 0

    def bytes_per_page_count(self):
        return self.file_size_in_bytes // self.bytes_per_page_count

    def do_something(self):
        pass

    def __str__(self):
        return f"{super().__str__()}, Format: {self.format}, File Size: {self.file_size_in_bytes} bytes"
