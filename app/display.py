from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> str:
        pass


class ConsoleDisplay(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    @staticmethod
    def displayy(book: Book) -> None:
        print(book.content[::-1])