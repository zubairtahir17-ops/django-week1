class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print("-" * 30)