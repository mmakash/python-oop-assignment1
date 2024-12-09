class Book:
    def __init__(self, book_id, title, author, availability=True, library=None):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

        if library:
            library.entry_book(self)

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__availability

    def borrowed_book(self):
        if self.__availability:
            self.__availability = False
            return f"Successfully borrowed '{self.__title}' by {self.__author}."
        else:
            return f"'{self.__title}' is not available."

    def returned_book(self):
        if not self.__availability:
            self.__availability = True
            return f"Successfully returned '{self.__title}' by {self.__author}."
        else:
            return f"'{self.__title}' was not borrowed."

    def view_book_info(self):
        status = "Available" if self.__availability else "Not Available"
        return f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Status: {status}"

    def __repr__(self):
        status = "Available" if self.__availability else "Not Available"
        return f"Id:{self.__book_id}, Title: {self.__title} by Author: {self.__author}, Status: {status}"


class Library:
    def __init__(self):
        self.__book_list = []

    def entry_book(self, book):
        if isinstance(book, Book):
            self.__book_list.append(book)
            print(f"Book '{book.get_title()}' by {book.get_author()} has been added.")
        else:
            print("Invalid input. Only Book objects are allowed.")

    def show_book(self):
        if self.__book_list:
            print("Books in the library:")
            for book in self.__book_list:
                print(book.view_book_info())
        else:
            print("No books available.")

    def find_book(self, book_id):
        for book in self.__book_list:
            if book.get_book_id() == book_id:
                return book
        return None


# Initialize library and books
my_library = Library()

book1 = Book(101, "Pother Panchali", "Bivuti Bhushon", library=my_library)
book2 = Book(102, "Putul Nacher Itikotha", "Manik Bondopadhaya", availability=False, library=my_library)
book3 = Book(103, "Hajar Bosor Dhore", "Johir Raihan", library=my_library)

# Menu-driven system
while True:
    print("\n--- Library Menu ---")
    print("1: View All Books")
    print("2: Borrow Book")
    print("3: Return Book")
    print("4: Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        my_library.show_book()
    elif choice == "2":
        try:
            book_id = int(input("Enter book ID to borrow: "))
            book = my_library.find_book(book_id)
            if book:
                print(book.borrowed_book())
            else:
                print("Book not found.")
        except ValueError:
            print("Invalid input! Please enter a valid book ID.")
    elif choice == "3":
        try:
            book_id = int(input("Enter book ID to return: "))
            book = my_library.find_book(book_id)
            if book:
                print(book.returned_book())
            else:
                print("Book not found.")
        except ValueError:
            print("Invalid input! Please enter a valid book ID.")
    elif choice == "4":
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
