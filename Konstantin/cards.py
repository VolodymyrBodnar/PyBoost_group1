import random
import itertools

class Card:
    class SUIT:
        diamond = "буби"
        hearts = "черви"
        spades = "пики"
        clubs = "трефы"
 
    class RANK:
        ace = "туз"
        jack = "валет"
        queen = "дама"
        king = "король"
        n_2 = "2"
        n_3 = "3"
        n_4 = "4"
        n_5 = "5"
        n_6 = "6"
        n_7 = "7"
        n_8 = "8"
        n_9 = "9"
        n_10 = "10"
 
    SUITS = (SUIT.diamond, SUIT.hearts, SUIT.spades, SUIT.clubs)
    RANKS = (RANK.ace, RANK.jack, RANK.queen, RANK.king, RANK.n_2, RANK.n_3, RANK.n_4,
             RANK.n_5,RANK.n_6, RANK.n_7, RANK.n_8, RANK.n_9, RANK.n_10)
 
    def __init__(self, suit, rank):
        if suit not in self.SUITS or rank not in self.RANKS:
            raise ValueError('Incorrect rank or suit.')
        self.suit = suit
        self.rank = rank
    

    def __add__(self, other):
        pass

cards = []
cards = [Card(suit, rank) for suit, rank in itertools.product(Card.SUITS, Card.RANKS)]
print (f"Сейчас в колоде {len(cards)} карты")

def deal_cart():
    index_cart = cards.pop(random.randint(0,len(cards)))
    print ('{}, {}'.format(index_cart.suit, index_cart.rank))
    print (f"В колоде осталось {len(cards)}")
    if index_cart.rank == 'валет' or index_cart.rank == 'дама' or index_cart.rank == 'король':
        index_cart.rank = 10
    elif index_cart.rank == 'туз':
        index_cart.rank = 11
    return index_cart.rank

def summ(num_of_cart):
    sum = 0
    for _ in range(num_of_cart):
        sum = sum + int(deal_cart())
    return sum
    

print(f"SUM - {summ(3)}")