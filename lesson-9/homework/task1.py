class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books (3).")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book} is already borrowed by someone else.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def __str__(self):
        books = ', '.join(str(book) for book in self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f"Member: {self.name}, Borrowed Books: {books}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book titled '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        book = self.find_book(book_title)
        member.return_book(book)

    def __str__(self):
        books = '\n'.join(str(book) for book in self.books)
        members = '\n'.join(str(member) for member in self.members)
        return f"Library Books:\n{books}\n\nLibrary Members:\n{members}"

# Test the Library Management System
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

    # Add members
    member1 = Member("Alice")
    member2 = Member("Bob")
    library.add_member(member1)
    library.add_member(member2)

    # Borrow books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Malcolm", "Outliers")
        library.borrow_book("Bob", "The Great Gatsby")
    except Exception as e:
        print(e)

    # Try exceeding borrow limit
    try:
        library.borrow_book("Alice", "The Great Gatsby")
    except Exception as e:
        print(e)

    # Return a book
    try:
        library.return_book("Alice", "1984")
        library.borrow_book("Alice", "The Great Gatsby")
    except Exception as e:
        print(e)

    # Display library status
    print(library)
