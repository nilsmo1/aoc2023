# Day 3, Gear Ratios

from typing import NamedTuple

# Q1
def cond(c):
    return not c.isdigit() and not c.isalpha() and c != '.'

def in_bounds(r, c, schema):
    return 0 <= r < len(schema) and 0 <= c < len(schema[r])

def symbol_neighbour(r, c, schema, cond):
    ids = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    return [cond(schema[r+rr][c+cc]) for cc, rr in ids if in_bounds(r+rr, c+cc, schema)].count(True)

def get_sum(schema):
    numbers = []
    for row, r in enumerate(schema):
        buffer = 0
        connected = False
        for col, c in enumerate(r):
            if c.isdigit():
                buffer = buffer * 10 + int(c)
                if symbol_neighbour(row, col, schema, cond):
                    connected = True
            if c == '.' or cond(c) or col == len(r) - 1:
                if connected: numbers.append(buffer)
                buffer = 0
                connected = False
    return sum(numbers)

# Q2
class Num(NamedTuple):
    value: int
    row  : int
    start: int
    end  : int
    def __eq__(self, other):
        return (self.row, self.start) == (other.row, other.start)


def get_numbers(schema):
    numbers = []
    for r, row in enumerate(schema):
        buffer = 0
        for c, char in enumerate(row):
            if char.isdigit():
                buffer = buffer * 10 + int(char)
            if not char.isdigit() or c == len(row)-1:
                if buffer:
                    numbers.append(Num(buffer, r, c-len(str(buffer)), c-1))
                buffer = 0
    return numbers

def get_neighbours(r, c, schema):
    found = []
    ids = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    neighbours = [(r+rr, c+cc) for rr, cc in ids if in_bounds(r+rr, c+cc, schema)]
    numbers = get_numbers(schema)
    for num in numbers:
        for row, col in neighbours:
            if row == num.row and num.start <= col <= num.end:
                found.append(num)
    return set(found)


def gear_ratio(schema):
    products = []
    for r, row in enumerate(schema):
        for c, char in enumerate(row):
            if char == '*':
                n = get_neighbours(r, c, schema)
                if len(n) != 2: continue
                n1, n2 = n
                products.append(n1.value * n2.value)
    return sum(products)


# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [line.strip() for line in inp.readlines()]


if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = get_sum(sample_input)
    t2 = gear_ratio(sample_input)
    assert t1 == 4361  , t1
    assert t2 == 467835, t2

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = get_sum(puzzle_input)
    q2 = gear_ratio(puzzle_input)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
