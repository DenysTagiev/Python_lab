class BookNotFoundException(Exception):
    def __init__(self, message="Book not found"):
        super().__init__(message)
