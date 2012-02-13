import math, time, mtools, sys, random

N = 100000

CC1 = 2
CC2 = 17
CC3 = 33
CH1 = 7
CH2 = 22
CH3 = 36
JAIL = 10
G2J = 30

cc_pile = range(1,17)
ch_pile = range(1,17)

def solve():
    return monopoly_sim(4)

def test():
    test_format()
    test_get_card()
    assert monopoly_sim(6) == '102400'

def monopoly_sim(sides):
    squares = [0 for i in range(40)]
    i = 0
    pos = 0
    doubles = 0
    while i < N:
        advance,double = roll_dices(sides)
        if double:
            doubles = doubles + 1
            if doubles == 3:
                doubles = 0
                pos = JAIL
                squares[pos] = squares[pos] + 1
                i = i + 1
                continue
        else:
            doubles = 0
        pos = pos + advance
        if pos >= 40:
            pos = pos % 40
        pos = deal_event(pos)
        if pos == JAIL:
            doubles = 0
        squares[pos] = squares[pos] + 1
        i = i + 1
    l = zip(range(len(squares)), squares)
    l.sort(cmp = lambda (p,c),(p2,c2): cmp(c,c2), reverse = True)
    show_rank(l)
    sl = [format_digits(l[i][0]) for i in range(3)]
    #print cc_pile, ch_pile
    r = ''.join(sl)
    print r
    return r

def show_rank(l):
    for i in range(3):
        print '%d = %.2f%%' % (l[i][0], float(l[i][1])/N*100)

def roll_dices(sides):
    d1 = random.randint(1, sides)
    d2 = random.randint(1, sides)
    return d1 + d2, d1 == d2

def deal_event(pos):
    if pos == G2J:
        return JAIL
    elif pos == CC1 or pos == CC2 or pos == CC3:
        card = get_card(cc_pile)
        if card == 1:
            return 0
        if card == 2:
            return JAIL
    elif pos == CH1 or pos == CH2 or pos == CH3:
        card = get_card(ch_pile)
        if card == 1:
            return 0
        if card == 2:
            return JAIL
        if card == 3:
            return 11
        if card == 4:
            return 24
        if card == 5:
            return 39
        if card == 6:
            return 5
        if card == 7 or card == 8:
            return next_rail(pos)
        if card == 9:
            return next_util(pos)
        if card == 10:
            return pos-3
    return pos

def next_rail(pos):
    if pos == CH1:
        return 15
    if pos == CH2:
        return 25
    if pos == CH3:
        return 5
    assert False

def next_util(pos):
    if pos == CH1:
        return 12
    if pos == CH2:
        return 28
    if pos == CH3:
        return 12
    assert False

def get_card(pile):
    card = pile[0]
    for i in range(1, len(pile)):
        pile[i-1] = pile[i]
    pile[len(pile)-1] = card
    return card

def format_digits(d):
    s = '%d' % d
    if d < 10:
        return '0' + s
    return s

def test_format():
    assert '00' == format_digits(0)
    assert '09' == format_digits(9)
    assert '10' == format_digits(10)

def test_get_card():
    cards = [1, 2, 3]
    c = get_card(cards)
    assert c == 1
    c = get_card(cards)
    assert c == 2
    c = get_card(cards)
    assert c == 3
    c = get_card(cards)
    assert c == 1

if __name__ == "__main__":
    test()
    t = time.time()
    print "answer = %s" % (solve())
    print "(%s)" % (time.time() - t)
