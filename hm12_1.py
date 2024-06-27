""" Task 1: deck """

import random


class Card:

    """ Class of cards: numbers and suits """

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def x1(self):

        """ for pylint :(, no need in code """

    def x2(self):

        """  for pylint :(, no need in code """


class CardsDeck:

    """ Create cards deck """

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        numbers = ['2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        for suit in suits:
            for number in numbers:
                self.deck.append(Card(number, suit))

    def shuffle(self):

        """ Create desc mix """

        random.shuffle(self.deck)

    def get(self, card_number):

        """ Get the card and show

         total result: card № and its suit """

        if 1 <= card_number <= len(self.deck):
            return (f"{self.deck[card_number - 1].suit} "
                    f"{self.deck[card_number - 1].number}")
        return "Неверный номер карты. Выберите число от 1 до 52."


deck = CardsDeck()
deck.shuffle()

card_number_x = int(input('Выберите карту из колоды в 52 карты: '))
card = deck.get(card_number_x)
print(f'Итого значение карты: {card}')
