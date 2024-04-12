from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import PrintConsole, PrintReverse
from app.serializer import BooksSerializerJson, BooksSerializerXML


commands_dict = {
    "display": {
        "console": ConsoleDisplay.display,
        "reverse": ReverseDisplay.display,
    },
    "print": {
        "console": PrintConsole.print_book,
        "reverse": PrintReverse.print_book,
    },
    "serialize": {
        "xml": BooksSerializerXML.serialize,
        "json": BooksSerializerJson.serialize,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        result = commands_dict[cmd][method_type](book)
    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
