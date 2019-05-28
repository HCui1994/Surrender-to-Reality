
from enum import Enum

Suit = Enum("Suit", ("Diamond", "Spade", "Club", "Heart"))


class Card(object):
    def __init__(self, suit: Suit, value: int, *args, **kwargs):
        self.suit = suit
        self.value = value
        return super().__init__(*args, **kwargs)


class Deck(object):
    def __init__(self, *args, **kwargs):
        self.deck = [Card(suit, value) for suit in Suit for value in range(1, 14)]
        self.status = [[1 for _ in range(13)] for _ in range(4)]

        return super().__init__(*args, **kwargs)

    def givecard(self) -> Card:
        import random
        if len(self.deck) == 0:
            # print("no card")
            # return None
            raise Exception()
        i = random.randint(len(self.deck))
        self.deck[i], self.deck[-1] = self.deck[-1], self.deck[i]
        card = self.deck[-1]
        self.status[card.suit.value - 1][card.val] = 0
        return self.deck.pop()

    def collect(self, card: Card):
        suit, val = card.suit, card.value
        if self.status[suit.value - 1][val]:
            print("collect failed")
            return
        
