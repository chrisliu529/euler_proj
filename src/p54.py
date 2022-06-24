import time

'''
    * High Card: Highest value card.
    * One Pair: Two cards of the same value.
    * Two Pairs: Two different pairs.
    * Three of a Kind: Three cards of the same value.
    * Straight: All cards are consecutive values.
    * Flush: All cards of the same suit.
    * Full House: Three of a kind and a pair.
    * Four of a Kind: Four cards of the same value.
    * Straight Flush: All cards are consecutive values of same suit.
    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
'''

HIGH_CARDS = 1
ONE_PAIR = 2
TWO_PAIRS = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9


def compare_hands(str_cards):
    cards = str_cards.split(' ')
    if len(cards) != 10:
        return 0
    hand1 = [make_card(c) for c in cards[:5]]
    hand2 = [make_card(c) for c in cards[5:]]
    p1 = parse_hand(hand1)
    p2 = parse_hand(hand2)
    if p1 > p2:
        return 1
    return 2


def make_card(c):
    value = c[0]
    color = c[1]
    special_vs = 'TJQKA'
    i = special_vs.find(value)
    if i < 0:
        return (int(value), color)
    return (10+i, color)


def check_dup(hv):
    assert len(hv) > 1
    v = hv[0]
    n = 0
    r = 0
    cr = 0
    for i in range(1, len(hv)):
        if hv[i] == v:
            n = n + 1
        else:
            if (n > r) or (n == r and v > cr):
                cr = v
                r = n
            v = hv[i]
            n = 0

    if (n > r) or (n == r and v > cr):
        cr = v
        r = n

    if r > 0:
        r = r + 1
        ret = cr, r, [x for x in hv if x != cr]
    else:
        ret = 0, 0, hv
    # print 'check_dup', hv, ret
    return ret


def values(h):
    return [x[0] for x in h]


def parse_hand(h):
    h.sort(key=lambda x: x[0], reverse=True)
    isf = is_flush(h)
    iss = is_straight(h)
    if isf and iss:
        return (STRAIGHT_FLUSH, h[0][0])
    if isf:
        return (FLUSH, values(h))
    if iss:
        return (STRAIGHT, h[0][0])
    hv = values(h)
    dup_card, dup_n, remain = check_dup(hv)
    if dup_n == 4:
        assert len(remain) == 1
        return (FOUR_OF_A_KIND, [dup_card] + remain)
    if dup_n == 3:
        assert len(remain) == 2
        rv = remain[0]
        if rv == remain[1]:
            return (FULL_HOUSE, [dup_card, rv])
        else:
            return (THREE_OF_A_KIND, [dup_card] + remain)
    if dup_n == 2:
        assert len(remain) == 3
        dup_card2, dup_n2, remain2 = check_dup(remain)
        if dup_n2 == 2:
            assert len(remain2) == 1
            return (TWO_PAIRS, [dup_card, dup_card2] + remain2)
        if dup_n2 == 0:
            return (ONE_PAIR, [dup_card] + remain)
    if dup_n == 0:
        assert len(remain) == 5
        return (HIGH_CARDS, remain)
    return 1


def is_flush(h):
    color = h[0][1]
    for i in range(1, len(h)):
        if color != h[i][1]:
            return False
    return True


def is_straight(h):
    start = h[0][0]
    for i in range(1, len(h)):
        if h[i][0] != start - i:
            return False
    return True


def solve():
    f = open('p054_poker.txt')
    s = f.read()
    lines = s.split('\n')
    cnt = 0
    for line in lines:
        res = compare_hands(line)
        if res == 1:
            cnt = cnt + 1
        print(f'{line} ({res})')
    return cnt


def parse_hand_sub(s):
    cards = s.split(' ')
    hand = [make_card(c) for c in cards]
    p = parse_hand(hand)
    # print s, p
    return p


def test():
    test_make_card()
    test_parse_hand()
    test_compare_hands()


def test_parse_hand():
    assert (STRAIGHT_FLUSH, 14) == parse_hand_sub('TS JS QS KS AS')
    assert (STRAIGHT, 14) == parse_hand_sub('TS JS QS KS AD')
    assert (FLUSH, [14, 13, 12, 11, 2]) == parse_hand_sub('2S JS QS KS AS')
    assert (STRAIGHT, 14) == parse_hand_sub('TS JS QS KS AD')
    assert (ONE_PAIR, [10, 14, 13, 12]) == parse_hand_sub('TS TH QS KS AD')
    assert (ONE_PAIR, [10, 14, 13, 12]) == parse_hand_sub('TS QS AD KS TH')
    assert (TWO_PAIRS, [12, 10, 14]) == parse_hand_sub('TS TH QS QH AD')
    assert (TWO_PAIRS, [12, 10, 14]) == parse_hand_sub('QS QH TS TH AD')
    assert (THREE_OF_A_KIND, [10, 14, 12]) == parse_hand_sub('TS TH TD QH AD')
    assert (FOUR_OF_A_KIND, [10, 14]) == parse_hand_sub('TS TH TD TC AD')
    assert (FULL_HOUSE, [10, 14]) == parse_hand_sub('TS TH TD AC AD')
    assert (FULL_HOUSE, [10, 14]) == parse_hand_sub('AC AD TS TH TD')
    assert (FULL_HOUSE, [10, 14]) == parse_hand_sub('AD TS TH AC TD')
    assert (HIGH_CARDS, [14, 11, 8, 7, 2]) == parse_hand_sub('AD JS 8H 7C 2D')


def test_make_card():
    assert (5, 'H') == make_card('5H')
    assert (13, 'D') == make_card('KD')
    assert (10, 'D') == make_card('TD')
    assert (14, 'S') == make_card('AS')
    assert (11, 'S') == make_card('JS')
    assert (2, 'D') == make_card('2D')


def test_compare_hands():
    assert 2 == compare_hands('5H 5C 6S 7S KD 2C 3S 8S 8D TD')
    assert 1 == compare_hands('5D 8C 9S JS AC 2C 5C 7D 8S QH')
    assert 2 == compare_hands('2D 9C AS AH AC 3D 6D 7D TD QD')
    assert 1 == compare_hands('4D 6S 9H QH QC 3D 6D 7H QD QS')
    assert 1 == compare_hands('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D')


if __name__ == "__main__":
    test()
    t = time.time()
    print(f"answer = {solve()}")
    print(f"({time.time() - t})")
