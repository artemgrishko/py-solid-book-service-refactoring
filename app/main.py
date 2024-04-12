from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import PrintConsole, PrintReverse
from app.serializer import BooksSerializerJson, BooksSerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay.display(book)
            elif method_type == "reverse":
                ReverseDisplay.display(book)
        elif cmd == "print":
            if method_type == "console":
                PrintConsole.print_book(book)
            if method_type == "console":
                PrintReverse.print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return BooksSerializerJson.serialize(book)
            if method_type == "xml":
                return BooksSerializerXML.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
