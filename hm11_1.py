""" Task 2: bank deposit """


class Book:

    """ Class has discription to one book """

    book_name = "Людзі на балоце"
    book_auth = "I.Мележ"
    book_page_amount = 300
    book_ISBN = "1234qwer"
    rsrved = False
    taken = False
    rsrved_by = None
    taken_by = None

    def about_book(self):

        """ Method return info status of reserv and taken """

        print(f"Статус 'в резерве': {self.rsrved} у {self.rsrved_by}")
        print(f"Статус 'на руках': {self.taken} у {self.taken_by}")
        return f"Книга '{self.book_name}' статус см.выше"

    def take_book(self, user):

        """ Method takes book to hands """

        if not self.taken:
            self.taken = True
            self.taken_by = user.user_name
            return f"Книга '{self.book_name}' теперь на руках {user.user_name}"
        return f"Книга '{self.book_name}' уже на руках"

    def reserve_book(self, user):

        """ Method reserves the book to hands """

        if not self.rsrved:
            self.rsrved = True
            self.rsrved_by = user.user_name
            return f"Книга '{self.book_name}' тепер reserved {user.user_name}"
        return f"Книгу '{self.book_name}' нельзя зарезервировать"

    def book_back_to_library(self, user):

        """ Method return the book form hands to library """

        if self.taken:
            user = self.taken_by
            self.taken_by = None
            self.taken = False
            return f"Теперь книга '{self.book_name}' сдана {user}"
        return f"Книга '{self.book_name}' в библиотеке, не на руках"

    def book_back_to_rsrved(self, user):

        """ Method return the book from reserv """

        if self.rsrved:
            user = self.rsrved_by
            self.rsrved_by = None
            self.rsrved = False
            return f"Теперь книга '{self.book_name}' снята с резерва {user}"
        return f"Книга '{self.book_name}' и так снята с резерва"


class BookUser:

    """ Class has discription for user """

    def __init__(self, user_name):

        self.user_name = user_name

    def x1(self):

        """ for pylint :(, no need in code """

    def x2(self):

        """  for pylint :(, no need in code """


book_user_1 = BookUser("Катя")
book_user_2 = BookUser("Дима")


book_1 = Book()

print("***** Резервируем книгу *****")
print(book_1.about_book())
print(book_1.reserve_book(book_user_1))
print(book_1.reserve_book(book_user_2))
print(book_1.book_back_to_rsrved(book_user_1))
print(book_1.reserve_book(book_user_2))
print(book_1.about_book())
print("***** Берём книгу *****")
print(book_1.about_book())
print(book_1.take_book(book_user_1))
print(book_1.take_book(book_user_2))
print(book_1.book_back_to_library(book_user_1))
print(book_1.take_book(book_user_2))
print(book_1.about_book())
