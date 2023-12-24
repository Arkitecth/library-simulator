class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self) -> None:
        self.shelf = []

    def add_books(self, book):
        if book.title not in self.shelf:
            self.shelf.append(book)
        else:
            print(f"{book} is already in Library")

    def remove_book(self, book):
        if book.title in self.shelf:
            self.shelf.remove(book)

    def search_book(self, title):
        for book in self.shelf:
            if book.title == title:
                return book

    def view_library(self):
        for book in self.shelf:
            print(book)


def main():
    library = Library()
    while True:
        user_input = int(input('''
        Welcome to the Library
                               
        1. Add Books
        2. Checkout Books 
        3. Search for a Book
        4. View Library
        5. Exit
                               
            ''')
                         )
        if user_input == 1:
            book_name = input("Please enter the book name: ")
            book_author = input("Please enter the books author: ")
            library.add_books(Book(book_name, book_author))
        elif user_input == 2:
            book_name = input(
                "What is the name of the book you would like to checkout: ")
            book = library.search_book(title=book_name)
            library.remove_book(book=book)
        elif user_input == 3:
            book_name = input(
                "What book are you searching for: ")
            book = library.search_book(title=book_name)
            if book:
                print(f"{book} was found")
            else:
                print(f"{book_name} was not found")
        elif user_input == 4:
            library.view_library()
        else:
            break


main()
