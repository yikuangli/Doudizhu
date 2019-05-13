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
            4：四带二
            8： 炸弹
            5： 顺子
            7：飞机
            6：连对
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
            return 8, 14
        else:
            if card[0]//4 == card[1]//4:
                return 2, card[0]//4 + 1
            else:
                return 0, 0

    def three(card):
        if card[0]//4 == card[1]//4 & & card[1] // 4 == card[2]//4:
            return 3, card[0]//4
        else:
            return 0, 0

    def threewone(card):
        minnum = card.remove(min(card))
        maxnum = card.remove(min(card))
        if three(minnum)[0]:
            return three(minnum)
        else:
            return three(maxnum)

    def threewtwo(card):
        card.sort()
        minp = card[:2]
        mint = card[2:]
        maxt = card[:3]
        maxp = card[3:]
        if not two(minp)[0] && not two(maxp)[0]:
            return 0, 0
        else:
            if three(maxt)[0]:
                return three(maxt)
            else:
                return three(mint)

    def four(card):
        if (sum(card)/4 - 2.5) % 4 == 0:
            return 8, min(card)//4 + 1
        else:
            return threewone(card)

    def five(card):
        if dragon(card) > 0:
            return 5, dragon(card)
        else:
            return threewtwo(card)

    def dragon(card):
        card.sort()
        previous = card[0]//4
        value = previous + 1
        for c in card:
            if c//4 != previous + 1 or c//4 >= 13:
                return 0
        return value

    def tuolaji(card):
        card.sort()
        previous = two(card[0:2])
        if(previous[0]):
            for i in range(0, len(Card), 2):
                now = two(card[i:i+2])
                if now[0] != 2 or now[1] != previous[1] + 1:
                    return 0,0
                else:
                    previous = now
            return 7,two(card[:2])
        else:
            return 0,0
    def airplane(card):
        card.sort()
        flag = True
        value = 0, 0
        if not len(card) % 3:
            previous = three(card[0:3])
            if(previous[0]):
                for i in range(0, len(Card), 3):
                    now = two(card[i:i+3])
                    if now[0] != 3 or now[1] != previous[1] + 1:
                        flag = False
             
        
    def card_checking(cards):
        draogon_checker = '34567890JQKA'
        value = [0 for x in range(14)]
        for c in cards:
            if c == 53 or c == 54:
                value[13 + c%53]
            else:
                value[c//4] += 1
        single = value
        double = list(map(lambda x: 1 if x >=2 else 0, value))
        triple = list(map(lambda x: 1 if x >=3 else 0, value))
        quadraple = list(map(lambda x: 1 if x >=4 else 0, value))
    
        for i,v in enumerate(value):
            if v:
                possible[1][v] = str(v)    
            if v > 1:
                possible[2][v] = str(v)*2 
            if v > 2:
                possible[3][v] = str(v)*3
                for c in value:
                    if c and c != v:
                        possible[31][v] = str(v)*3 + str(c)
                for c in value:
                    if c > 2 and c != v:
                        possible[31][v] = str(v)*3 + str(c)*2
            if v > 3:
                possible[4][v] = str(v)*4 
                
        dragon = value[:-2]
        dragon.append(0)
        tuolaji = [x-1/x-1 for x in value[:-3]]
        tuolaji.append(0)
        airp = [x-2/x-2 for x in value[:-3]]
        airp.append(0)
        nd,nt,na = 0
        for i,v in enumerate(dragon):
            if not v:
                if i - nd >= 5:
                    d[5].append((nd,i - nd))
                nd = i + 1
        for i,v in enumerate(tuolaji):
            if not v:
                if i - nt >= 3:
                    d[6].append((nt,i - nt))
                nt = i + 1
        for i,v in enumerate(airp):
            if not v:
                if i - na >= 2:
                    d[5].append((na,i - na))
                na = i + 1

    def generate_helper(v,i,t,ex):
        if v >= t and i not in ex:
            return 1
        else:
            return 0
    def valid_move(self, card):
