# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

newSelf = []

class Library:

  def __init__(self, *name):
    for i in name:
      newSelf.append(i)

  def show(self):
    print(newSelf)

  def outBook(self):
    outbook = (input("insert book name you want: "))
    newSelf.remove(outbook)


a = Library("Abhay", "Harry", "Rohan", "Vinay")
a.show()
a.outBook()
a.show()