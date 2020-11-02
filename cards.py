
class Card:
    class SUIT:
        diamond = "diamonds"
        hearts = "hearts"
        spades = "spades"
        clubs = "clubs"
 
    class RANK:
        ace = "ace"
        jack = "jack"
        queen = "queen"
        king = "king"
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
    RANKS = (RANK.ace, RANK.jack, RANK.queen,
             RANK.king, RANK.n_2, RANK.n_3, RANK.n_4,
             RANK.n_5,RANK.n_6, RANK.n_7, RANK.n_8,
             RANK.n_9, RANK.n_10)
 
    def __init__(self, suit, rank):
        if suit not in self.SUITS or rank not in self.RANKS:
            raise ValueError('Incorrect rank or suit.')
        self.suit = suit
        self.rank = rank
    
    def __add__(self, other):
        pass
