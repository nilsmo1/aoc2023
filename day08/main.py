# Day 8, Haunted Wasteland

# Q1
def follow_instructions(t):
    inst, d = t
    i = 0
    c = 'AAA'
    dir = {'L': 0, 'R': 1}
    while c != 'ZZZ':
        c = d[c][dir[inst[i % len(inst)]]]
        i += 1
    return i


# Q2

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        sp = [g for g in inp.read().split('\n\n')]
        inst = sp[0]
        raw = [line.split() for line in sp[1].split('\n') if line]
    d = {}
    for s, _, l, r in raw:
        s = s.strip()
        l = l[1:-1].strip()
        r = r.strip()[:-1]
        d[s] = (l, r)
    return inst, d


if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = follow_instructions(sample_input)
    t2 = 0
    assert t1 == 6, t1
    assert t2 == 0, t2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = follow_instructions(puzzle_input)
    q2 = 0
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
