# Day 4, Scratchcards

# Q1
def solve():
    pass

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

    # Puzzle input
    #puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: ')
    print(f'Q2: ')
