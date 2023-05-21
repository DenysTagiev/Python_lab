from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title="", author="", publisher="", year=0, genre=""):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        
    BYTES_PER_PAGE_COUNT = 1024

    @abstractmethod
    def book(self, quantity):
        pass

    @abstractmethod
    def has_more_books(self):
        pass

    @abstractmethod
    def BYTES_PER_PAGE_COUNT(self):
        pass

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}"