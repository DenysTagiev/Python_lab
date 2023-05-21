from paper_book import  PaperBook
from electronic_book import ElectronicBook

class book_manager(PaperBook, ElectronicBook):
    
    def main():
        books = [PaperBook("Father", "Maks", "Ivan", 2005, "Novel", 130, 300, 150, 200),
                ElectronicBook("Sample", "John", "ABC", 2022, "Fiction", 100, "PDF", 1920)]

        for book in books:
            print(book)
               
if __name__ == "__main__":
     book_manager.main()   
     