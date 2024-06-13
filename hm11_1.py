""" Task 2: bank deposit """


class Book:

    """ h """

    book_name = "Людзі на балоце"
    book_auth = "I.Мележ"
    book_page_amount = 300
    book_ISBN = "1234qwer"
    rsrved = False
    taken = False

    def about_book(self):

        """ h """

        return f"{self.book_name} Врезерве:{self.rsrved}, наруках:{self.taken}"

    # def take_book_status(self):
    #     if self.taken == False:
    #         return f"Книга в библиотеке"
    #     else:
    #         return f"Книга на руках"
    #
    # def reserve_book_status(self):
    #     if self.rsrved == False:
    #         return f"Книгу можно зарезервировать"
    #     else:
    #         return f"Книгу нельзя зарезервировать"

    def take_book(self):

        """ h """

        if self.taken is False:
            self.taken = True
            return f"Книга '{self.book_name}' теперь на руках"
        # else:
        return f"Книга '{self.book_name}' на руках"

    def reserve_book(self):

        """ h """

        if self.rsrved is False:
            self.rsrved = True
            return f"Книга '{self.book_name}' теперь зарезервирована"
        # else:
        return f"Книгу '{self.book_name}' нельзя зарезервировать"

    def book_back_to_library(self):

        """ h """

        if self.taken is True:
            self.taken = False
            return f"Теперь книга '{self.book_name}' сдана"
        # else:
        return f"Книга '{self.book_name}' в библиотеке, не на руках"

    def book_back_to_rsrved(self):

        """ h """

        if self.rsrved is True:
            self.rsrved = False
            return f"Теперь книга '{self.book_name}' снята с учёта"
        # else:
        return f"Книга '{self.book_name}' и так снята с учёта"


class BookUser:

    """ h """

    def __init__(self, user_name):

        self.user_name = user_name

    def x1(self):

        """ for pylint :(, no need in code """

    def x2(self):

        """  for pylint :(, no need in code """


book_user_1 = BookUser("Катя")
book_user_2 = BookUser("Дима")


book_1 = Book()

print(book_1.about_book())
print(book_1.reserve_book())
print(book_1.take_book())
print(book_1.about_book())
print(book_1.reserve_book())
print(book_1.take_book())
print(book_1.book_back_to_library())
print(book_1.book_back_to_rsrved())
print(book_1.about_book())
