class Book:
    def __init__(self,book_id,title,author,availability = True,library = None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

        if library:
            library.entry_book(self)

    def borrowed_book(self):
        if self.availability:
            self.availability = False
            return f"successfully borrowed {self.title} by {self.author} book"
        else:
            return f"this {self.title} book is not available"
    def returned_book(self):
        if not self.availability:
            self.availability = True
            return f"successfully returnd {self.title} by {self.author} book"
        else:
            return f"this {self.title} book was not borrowed"

    def view_book_info(self):
        status = "Available" if self.availability else "Not Available"
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nStatus: {status}"

    def __repr__(self):
        status = "Available" if self.availability else "Not available"
        return f"Id:{self.book_id}, title: {self.title} by author: {self.author},Status: {status}"
    
class Library:
    book_list = []

    def entry_book(self,book):
        if isinstance(book,Book):
            self.book_list.append(book)
            print(f"Book {book.title} by {book.author} has been added")
        else:
            print("Invalid input,Only Book object allow here")

    def show_book(self):
        if self.book_list:
            print("book in the library")
            for book in self.book_list:
                print(f"-{book.title} by {book.author}")
        else:
            print(f"no books available")
    
    def find_book(self,book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                return book
        return None

my_library = Library()

book1 = Book(101, "1984", "George Orwell", library=my_library)
book2 = Book(102, "To Kill a Mockingbird", "Harper Lee", availability=False, library=my_library)
book3 = Book(103, "The Great Gatsby", "F. Scott Fitzgerald", library=my_library)



while True:
    print("\n---library menu---")
    print("1: view all books")
    print("2: borrow book")
    print("3: returned book")    
    print("4: exit")    
    click = input("enter your choice(1-4): ")

    if click == "1":
        my_library.show_book()
    elif click == "2":
        try:
            book_id = int(input("enter book_id to borrow: "))
            book = my_library.find_book(book_id)
            if book:
                print(book.borrowed_book())
            else:
                print("book not found")
        except ValueError:
            print("invalid input!")
    elif click == "3":
        try:
            book_id = int(input("enter book_id to return: "))
            book = my_library.find_book(book_id)
            if book:
                print(book.returned_book())
            else:
                print("book not found")
        except ValueError:
            print("Invalid input!")

    elif click == "4":
        print("existing the library system,goodbye")
        break
    else:
        print("invalid choice , write valid choice")
