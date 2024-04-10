from marcos.main import Book

# Usage
book = Book("1984", "George Orwell", 328, 200)
print(book)
book.say_hello("oi")
print("------")
book.say_sum(book.pages, book.weight)
