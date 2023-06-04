from Models.Book import Book


class PaperBook(Book):
    def __init__(self, title="", author="", publisher="", year=0, genre="", count_in_warehouse=0, pages=0, size_width=0, size_height=0):
        super().__init__(title, author, publisher, year, genre)
        self.count_in_warehouse = count_in_warehouse
        self.pages = pages
        self.size_width = size_width
        self.size_height = size_height

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
        return self.pages

    def do_something(self):
        return f"Do something with {self.title}"

    def __str__(self):
        return f"{super().__str__()}, Pages: {self.pages}, Size: {self.size_width}mm x {self.size_height}mm"

