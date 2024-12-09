class Book:
    def __init__(self,book_id,title,author,availability = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def __repr__(self):
        status = "Available" if self.availability else "Not available"
        return f"Id:{self.book_id}, title: {self.title} by author: {self.author},Status: {self.availability}"
    
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
    
my_library = Library()
book1 = Book(101, "1984", "George Orwell")
book2 = Book(102, "To Kill a Mockingbird", "Harper Lee", availability=False)
my_library.entry_book(book1)
my_library.entry_book(book2)
my_library.show_book()
