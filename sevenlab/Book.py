from abc import ABC, abstractmethod
class Book(ABC):
    BYTES_PER_PAGE_COUNT = 1920
    
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
    
    def BYTES_PER_PAGE_COUNT(self):
        pass
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}, Genre: {self.genre}"