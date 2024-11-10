class Book:
    def __init__(self,title,author,is_borrowed):
       self.title = title
       self.author = author
       self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    
    class Library_member:
     def Library_member (self,name,member_id,):
         self.name = name
         self.member_id = member_id
         self.borrowed_books = []


     def borrow_book(self, book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} successfully returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book.title} by {book.author}")
        else:
            print (f"{self.name} has not borrowed any books.")


      

 



