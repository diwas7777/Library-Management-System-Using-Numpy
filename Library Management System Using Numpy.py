import numpy as np

class LibraryManagementSystem:
    def __init__(self) -> None:
        self.user = np.array([""])
        self.userBook = np.asarray([["",""]])

    def decision(self):
        print("Type an option from the following choice")
        print("1. View User List\n2. View User, Book List\n3. Take a book\n4. Return Book\n5. Exit")
        choice = int(input("Choice?: "))
        if choice == 1:
            self.userList()

        elif choice == 2:
            self.userBookList()

        elif choice == 3:
            self.userBookRegister()
        
        elif choice == 4:
            self.returnBook()

        elif choice == 5:
            exit()

        else:
            print("That choice is currently unavailable")

    def userList(self) -> None:
        print("Users List: ")
        for users in self.user:
            print(users)
        self.decision()

    def userBookList(self):
        print("User, Book List")
        for items in self.userBook:
            print(items)
        self.decision()

    def userBookRegister(self) -> None:
        username = input("Enter the name of user: ").upper()
        bookname = input("Enter name of the book you want to take: ").upper()   
        if(np.where(np.where(self.userBook == [username, bookname])[1])[0].size > 0):
            print(f"User: {username} has already taken {bookname} book.")
        else:
            self.userBook = np.append(self.userBook, np.asarray([[username, bookname]]), axis = 0)
            print(f"Book: {bookname} has been registered for User: {username}")
        if(len(np.where(self.user == username)[0]) == 0):
            self.user = np.append(self.user, username)
            print(f"User: {username}, has been added to Users List")
        self.decision()

    def returnBook(self) -> None:
        username = input("Enter name of the user: ").upper()
        bookname = input("Enter name of the book you want to return: ").upper()
        loopcheck = 0
        print(np.where(self.userBook == [username, bookname])[1])
        for items in range(len(np.where(self.userBook == [username, bookname])[1])):            
            if(np.where(self.userBook == [username, bookname])[1][items] == 1):
                self.userBook = np.delete(self.userBook, items, axis=0)
                print(f"User: {username} has returned book: {bookname}, successfully.")
                loopcheck = 1
        if(loopcheck == 0):
            print(f"User: {username} OR Book: {bookname}, not found.")
        self.decision()


diwas = LibraryManagementSystem()
diwas.decision()