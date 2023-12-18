# Day 7, Camel Cards

from collections import Counter, defaultdict
from functools import cmp_to_key


# Q1
def score_hand(hand):
    c = Counter(hand)
    common = c.most_common(2)
    if len(common) == 1: return 7
    (_, v1), (_, v2) = c.most_common(2)
    pairs = [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)]
    for i, (c1, c2) in enumerate(pairs):
        if v1 == c1 and v2 == c2: return i + 1


def compare(h1, h2):
    vs = "23456789TJQKA"
    h1, h2 = h1[0], h2[0]
    for c1, c2 in zip(h1, h2):
        v1, v2 = vs.index(c1), vs.index(c2)
        if v1 > v2: return 1
        elif v1 < v2: return -1
    return 0


def sort_hands(hands):
    dd = defaultdict(list)
    for hand, bid in hands:
        dd[score_hand(hand)].append((hand, bid))
    q = [d for i in range(1, 8) for d in sorted(dd[i], key=cmp_to_key(compare))]
    return sum(d[1]*(i+1) for i, d in enumerate(q))


# Q2
# if hand not in 3 1, 2 2, 


def rescore(hand):
    if 'J' not in hand: return score_hand(hand), hand
    vs = "J23456789TQKA"
    c = Counter(hand)
    mcs = c.most_common(5)
    mc, v = mcs[0]
    if mc == 'J' and v == 5:
        return score_hand(hand.replace('J', 'A')), hand.replace('J', 'A')
    elif mc == 'J':
        mc2, v2 = mcs[1] # idk anymore

    if v == 1:
        hand = hand.replace('J', max(mcs, key=lambda x: vs.index(x[0]))[0])
    elif v == 2:
        mc2, v2 = mcs[1]
        if v2 == 2:
            if vs.index(mc) > vs.index(mc2):
                hand = hand.replace('J', mc)
            else: hand = hand.replace('J', mc2)
    else:
        hand = hand.replace('J', mc)
    return score_hand(hand), hand


def compare2(h1, h2):
    vs = "J23456789TQKA"
    h1, h2 = h1[0], h2[0]
    for c1, c2 in zip(h1, h2):
        v1, v2 = vs.index(c1), vs.index(c2)
        if v1 > v2: return 1
        elif v1 < v2: return -1
    return 0

def sort_hands2(hands):
    dd = defaultdict(list)
    for hand, bid in hands:
        new_t, new_h = rescore(hand)
        if 'J' in new_h: print(new_h)
        dd[new_t].append((new_h, bid))
    q = [d for i in range(1, 8) for d in sorted(dd[i], key=cmp_to_key(compare2))]
    #for c in q: print(c)
    return sum(d[1]*(i+1) for i, d in enumerate(q))


# Input
def parse_input(file):
    with open(file, 'r') as inp:
        raw = [line.split() for line in inp.readlines() if line]
    return [(hand, int(bid)) for hand, bid in raw]


if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = sort_hands(sample_input)
    t2 = sort_hands2(sample_input)
    assert t1 == 6440, t1
    assert t2 == 5905, t2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = sort_hands(puzzle_input)
    q2 = sort_hands2(puzzle_input)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
