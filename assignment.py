class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"
    
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
book1 = Book("hridoye megh","bakibillah saheb")
book2 = Book("kill your comfort","barish thakur")
my_library.entry_book(book1)
my_library.entry_book(book2)
my_library.show_book()
