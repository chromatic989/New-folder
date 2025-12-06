class library:
    def __init__(self, books, name):
        self.books = books
        self.name = name
        self.lent_books = {}

    def display_books(self):
        print(f"books available in{self.name}")
        for book in self.books:
            print(f"-{book}")

    def lend_book(self,user,book):
        if book not in self.books:
            print("❌ book not found in library")

        elif book in self.lent_books:
            print("book already lent to{self.lent_book[book]}.")

        else:
            self.lent_books[book] = user
            print("✅ book has been lent to you")

    def add_book(self,book):
        self.books.append(book)
        print("✅ book added succsesfully")

    def return_book(self,book):
        if book in self.lent_books:
           del self.lent_books[book]
           print("✅book returned thank you!")
        else:
            print("❌this book was borrowed")

if __name__ == "__main__":
    library = library(
        ["python", "harry potter","wings of the fire","wimpy kid","c++ coding"]
    )

user = input("enter your name: ")
 
while True:
    print("/n 1.display books /n2.Lend books /n3.Add book /n4. Return book /n5. Quit ")

    choice = input("chose an option:")

    if choice == '1':
        library.display_books
    elif choice == '2':
        library.add_book()
    elif choice == '3':
        library.return_book()
    elif choice == '4':
        library.quit_book()
    else:
       print("❌ wrong chice goodbye!")