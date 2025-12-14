# Class utente

class User:
    def __init__(self, name):
        self.name = name
        self.loaned_books = []
        self.loan_limit = 5
        self.user_id = None
