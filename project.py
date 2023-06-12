class Book():
    def __init__(self,Unique_ID,Title,Author,Level):
        self.Unique_ID = Unique_ID
        self.Title = Title
        self.Author = Author
        self.Level = Level
        self.Availability_status = True
class Member():
    def __init__(self,Unique_ID,Name,Email,Level):
        self.Unique_ID = Unique_ID
        self.Name = Name
        self.Email = Email
        self.Level = Level
        self.List_of_borrowed_books =[]
class Libray():
    def __init__(self):
        self.books = []
        self.members = []

    def Add_Member(self,member):
        self.members.append(member)

    def Edit_Member(self, Member_ID, Name=None, Email=None, Level=None):
        member = self.Find_Member(Member_ID)
        if name:
            member.Name = Name
        if email:
            member.Email = Email
        if level:
            member.Level = Level

    def Show_Members(self):
        if len(self.members)==0:
            print("no member")
        else:
            print("List of Members:")
            print('ID  |   Name    |   Email          |   Level ')
            for member in self.members:
                print(f"{member.Unique_ID}\t|\t{member.Name}\t|\t{member.Email}\t|\t{member.Level}")
            print("-----------------------------------------------------------")
    def Delete_Member(self, Member_ID):
        member = self.Find_Member(Member_ID)
        self.members.remove(member)

    def Add_Book(self, book):
        self.books.append(book)

    def Show_Books(self):
        if len(self.books)==0:
            print("NO Books")
        else:
            print("List of Books:")
            print('ID  |   Title    |   Author    |   Level |  Availability_status  ')
            for book in self.books:
                print(f"{book.Unique_ID}\t|\t{book.Title}\t|\t{book.Author}\t|\t{book.Level}\t|\t{book.Availability_status}")
            print("-----------------------------------------------------------")
    def Find_Book(self, Book_ID):
        for book in self.books:
            if Book_ID == Book_ID:
                return book
        return None

    def Find_Member(self, Member_ID):
        for member in self.members:
            if member.Unique_ID == Member_ID:
                return member
        return None

    def Borrow_Book(self, Member_ID, Book_ID):
        member = self.Find_Member(Member_ID)
        book = self.Find_Book(Book_ID)
        if book and book.Availability_status and member.Level >= book.Level:
            book.Availability_status = False
            member.List_of_borrowed_books.append(book)
            print(f"{member.Name} has successfully borrowed {book.Title}.")
        elif not book:
            print("Book not found.")
        elif not book.Availability_status:
            print("Book is not available for borrowing.")
        elif member.Level < book.Level:
            print("The book is not appropriate for the member's level.")

    def Return_Book(self, Member_ID, Book_ID):
        member = self.Find_Member(Member_ID)
        book = self.Find_Book(Book_ID)
        if book in member.List_of_borrowed_books:
            book.Availability_status = True
            member.List_of_borrowed_books.remove(book)
            print(f"{member.Name} has successfully returned {book.Title}.")
        else:
            print("The member did not borrow the book.")


libray=Libray()
while True:
    print('------------------------------------ Wlcome to the Library System ------------------------------------------------------')
    print('1. Add Member \n2.Edit Member \n3.Show Members \n4-Delete Member \n5.Add Book \n6.Show Books \n7.Borrow Book \n8.Return Book \n9.Exit')
    Choise_num=int(input("Enter your choice: "))
    if Choise_num == 1 :
        ID = int(input("*Enter member ID: "))
        name = input("*Enter Member name: ")
        email = input("*Enter Member email: ")

        while True:
            level = input("*Enter the member level(A/B/C): ")
            if level.upper() == 'A' or level.upper() == 'B' or level.upper() == 'C':
                member = Member(ID, name, email, level)
                libray.Add_Member(member)
                print("#Member added successfully.")
                break
            else:
                print("try again")

    elif Choise_num == 2:
        member_id = int(input("Enter member ID: "))
        member = libray.Find_Member(member_id)
        if member:
            name = input("Enter new name: ")
            email = input("Enter new email: ")

            while True:
                level = input("Enter new level (A/B/C): ")
                if level.upper() == 'A' or level.upper() == 'B' or level.upper() == 'C':
                    libray.Edit_Member(member_id, name, email, level)
                    print("Member edited successfully.")
                    break
                else:
                    print("try again")


        else:
            print("Member not found.")
    elif Choise_num == 3:
        libray.Show_Members()
    elif Choise_num == 4:
        member_id = int(input("Enter member ID: "))
        member = libray.Find_Member(member_id)
        if member:
            libray.Delete_Member(member_id)
            print("Member deleted successfully.")
        else:
            print("Member not found.")
    elif Choise_num == 5:
        id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        while True:
            level = input("Enter book level (A/B/C): ")
            if level.upper() == 'A' or level.upper() == 'B' or level.upper() == 'C':
                book = Book(id, title, author, level)
                libray.Add_Book(book)
                print("Book added successfully.")
                break
            else:
                print("try again")
    elif Choise_num == 6:
        libray.Show_Books()
    elif Choise_num == 7:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        libray.Borrow_Book(member_id, book_id)
    elif Choise_num == 8:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        libray.Return_Book(member_id, book_id)
    elif Choise_num == 9:
        break
    else:
        print("Invalid choice. Please try again.")