from library import Book

# Creating three Book objects

book1 = Book("Atomic Habits", "James Clear")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Deep Work", "Cal Newport")

# Displaying information about all three books

print("LIBRARY BOOK COLLECTION")
print("=" * 30)

book1.describe()
book2.describe()
book3.describe()