# Classe biblioteca
from book import Book
from user import User

class Library:
    book_start_id = 1000
    user_start_id = 1
    
    def __init__(self, name):
        self.name = name
        self.books_list = []
        self.users_list = []

    def add_book(self, book):
        self.books_list.append(book)
        book.isbn = Library.book_start_id
        Library.book_start_id += 1

    def add_user(self, user):
        user.user_id = Library.user_start_id
        self.users_list.append(user)
        Library.user_start_id += 1

    def find_book(self, isbn):
        for book in self.books_list:
            if book.isbn == isbn:
                return book
        return f"Error: Book not found"
            
    def find_user(self, user_id):
        for user in self.users_list:
            if user.user_id == user_id:
                return user
        return f"Error: User not found"
    
    def loan_book(self, isbn, user_id):
        found_book = self.find_book(isbn)
        if found_book == "Error: Book not found":
            return "Error: Book not found"
        found_user = self.find_user(user_id)
        if found_user == "Error: User not found":
            return "Error: User not found"

        if not found_book.is_loaned:
            if len(found_user.loaned_books) < found_user.loan_limit:
                found_user.loaned_books.append(found_book)
                found_book.is_loaned = True
                return f"Book: {found_book.title} loaned to {found_user.name}"
            return f"Error: {found_user.name} can't loan book anymore. Loan limit is: {found_user.loan_limit}"
        return f"Error: book is already loaned"
    
    def return_book(self, isbn, user_id):
        found_book = self.find_book(isbn)
        if found_book == "Error: Book not found":
            return "Error: Book not found"
        found_user = self.find_user(user_id)
        if found_user == "Error: User not found":
            return "Error: User not found"
        
        if not found_book.is_loaned:
            return "Error: Book isn't loaned"

        if found_book in found_user.loaned_books:
            found_user.loaned_books.remove(found_book)
            found_book.is_loaned = False
            return f"Book successfully returned to library"
        return f"Error: Book isn't loaned to user: {found_user.name}"
    



    
        











