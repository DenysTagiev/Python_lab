class Book:
    def __init__(self, title="", author="", publisher="", year=0, genre="", count_in_warehouse=0):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.count_in_warehouse = count_in_warehouse

    def get_book(self, quantity):
        if self.count_in_warehouse >= quantity:
            self.count_in_warehouse -= quantity
            return quantity
        else:
            available_books = self.count_in_warehouse
            self.count_in_warehouse = 0
            return available_books

    def has_more_books(self):
        return self.count_in_warehouse > 0

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}, Count in Warehouse: {self.count_in_warehouse}"

if __name__ == "__main__":
    
    book = Book("Назва книги", "Автор книги", "Видавець книги", 2021, "Жанр книги", 8)

    print(book.get_book(5))  # Виводиться: 5
    print(book.has_more_books())  # Виводиться: True
    print(book.get_book(5))  # Виводиться: 5
    print(book.has_more_books())  # Виводиться: False

    books = []

    books.append(Book())
    books.append(Book("Father", "Maks", "Ivan", 2005, "Novel", 130))
    books.append(Book())
    books.append(Book())

    for book in books:
        print(book)