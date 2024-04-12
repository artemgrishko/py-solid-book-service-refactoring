from abc import abstractmethod, ABC

from app.book import Book


class PrintBook(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> str:
        pass


class PrintConsole(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
