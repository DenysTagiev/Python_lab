from abc import ABC, abstractmethod


class Book(ABC):
    bytes_per_page_count = 1920

    def __init__(self, title="", author="", publisher="", year=0, genre=""):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre

    @abstractmethod
    def book(self, quantity):
        pass

    @abstractmethod
    def has_more_books(self):
        pass

    @abstractmethod
    def bytes_per_page_count(self):
        pass

    @abstractmethod
    def do_something(self):
        pass

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}"
