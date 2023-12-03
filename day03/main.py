# Day 3, Gear Ratios
import re

# Q1
def get_num_ids(schema):
    ids = [[(m.start(), m.end()-1, int(line[m.start():m.end()])) for i, m in enumerate(re.finditer(r"\d+", line))]
           for line in schema]
    return ids

def get_symbols(schema):
    symbs = [[i for i, e in enumerate(r) if e in "*+/&"] for r in schema]
    return symbs

def get_sum(schema):
    ids = get_num_ids(schema)
    symbs = get_symbols(schema)
    for i, id in enumerate(ids):
        for s in symbs:


# Q2

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [line.strip() for line in inp.readlines()]


if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = get_sum(sample_input)

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    print(f'Q1: ')
    print(f'Q2: ')
