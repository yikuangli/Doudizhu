import random


class Card:
    deck = []
    user1 = []
    user2 = []
    user3 = []
    bottom = []
    last = []
    DECK_LENGTH = 54

    def __init__(self):
        self.deck = [i for i in range(53)]
        shuffle()
        dial()
        landlord()

    def shuffle(self):
        random.shuffle(self.deck)

    def dial(self):
        self.user1 = self.deck[:17]
        self.user2 = self.deck[17:34]
        self.user3 = self.deck[34:51]

    def convert_real_Value(self, card):
        """
            return tuple, first type, second value.
            Type table:
            1: 单张
            2: 对子
            3: 三带零/一/二
            4：四带单/四带二
            0： 炸弹
            5： 顺子
            6：飞机
            7：连对

        """
        return {
            1: one(self.card),
            2: two(self.card),
            3: three(self.card),
            4: four(self.card),
            5: five(self.card),
            6: six(self.card)
        }.get(len(self.card), abunch(self.card))

        if len(card) == 2 & & card[0] + card[1] == 105:
            return 4, 14
        if len(card) == 1:

        if

    def one(card):
        return 1, {
            52: 14,
            53: 15
        }.get(card[0], card[0]//4 + 1)
    def two(card):
        if card[0] + card[1] == 107:
            return 0, 14
        else:
            if card[0]//4 == card[1]//4:
                return 2, card[0]//4
            else: 
                return -1, -1
    def three(card):
        if card[0]//4 == card[1]//4 && card[1] //4 == card[2]//4:
            return 3, card[0]//4
        else:
            return -1, -1
    def threewone(card):
        minnum = card.remove(min(card))
        maxnum = card.remove(min(card))
        if three(minnum)[0] != -1:
            return three(minnum)
        else:
            return three(maxnum)
    

        return 
    def four(card):
        if (sum(card)/4 - 2.5)% 4 == 0:
            return 0,min(card)//4 + 1
        else:
            return threewone(card)
    def five(card):
        if 
        
    def valid_move(self, card):
