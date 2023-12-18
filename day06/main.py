# Day 6, Wait For It

from math import sqrt, ceil, floor

# Q1
def winning_ways(ls):
    ways = 1
    for t, d in ls:
        pass
        # nvm this becomes sad
        # th * (t-th) > d
        # ->
        # th*t - th^2 - d = 0
        # th^2 - t*th + d = 0
        # th = t/2 +- sqrt(t/2 ^ 2 - d)
        # th0 = t/2 + sqrt(t/2 ^ 2 - d)
        # th1 = t/2 - sqrt(t/2 ^ 2 - d)
        th0 = int(t/2 - sqrt(t*t/4 - d)+1)
        th1 = int(t/2 + sqrt(t*t/4 - d)-1)
        #print(t, d, th0, th1)
        L = th0
        R = th1
        formula = lambda x: x*(t-x) > d
        fL = formula(L)
        fR = formula(R)
        while fL or fR:
            if fL:
                L -= 1
                fL = formula(L)
            if fR:
                R += 1
                fR = formula(R)
        R -= 1
        L += 1
        ways *= (R-L+1)
    return ways

# Q2
def larger_wins(ls):
    t = ""
    d = ""
    for t0, d0 in ls:
        t += str(t0)
        d += str(d0)
    return winning_ways([(int(t), int(d))])


# Input
def parse_input(file):
    with open(file, 'r') as inp:
        raw = [line.split() for line in inp.readlines()]
    ls = [(int(t), int(d)) for t, d in zip(raw[0][1:], raw[1][1:])]
    return ls


if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = winning_ways(sample_input)
    t2 = larger_wins(sample_input)
    assert t1 == 288  , t1
    assert t2 == 71503, t2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = winning_ways(puzzle_input)
    q2 = larger_wins(puzzle_input)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
