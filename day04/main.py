# Day 4, Scratchcards

# Q1
def solve(cards):
    score = 0
    for nums, winning in cards:
        wins = len([e for e in winning if e in nums])
        if not wins: continue
        score += 2**(wins-1)
    return score

# Q2

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        raw = inp.readlines()
    lines = []
    for line in raw:
        no_card = line.split(':')[1]
        no_bar = no_card.split('|')
        spaces = [[int(c) for c in part.split()] for part in no_bar]
        lines.append(spaces)
    return lines

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = solve(sample_input)
    assert t1 == 13, t1

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = solve(puzzle_input)
    q2 = None
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
