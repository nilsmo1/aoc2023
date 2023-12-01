# Day 1, Trebuchet?!
from typing import List
import re

# Q1
def get_sum(doc: List[str]) -> int:
    return sum(int(d[0]+d[-1]) if d else 0 for d in [[e for e in l if e.isdigit()] for l in doc])

# Q2
def get_sum2(doc: List[str]) -> int:
    ds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    res = 0
    for line in doc:
        di = {}
        for i, d in enumerate(ds):
            occs = [m.start() for m in re.finditer(d, line)]
            for occ in occs: di[occ] = str(i+1)
        for i, c in enumerate(line):
            if c.isdigit(): di[i] = c
        l, r = di[min(di)], di[max(di)]
        res += int(l+r)
    return res

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [line.strip() for line in inp.readlines()]


if __name__ == '__main__':
    # Samples
    sample_input1 = parse_input('sample1')
    sample_input2 = parse_input('sample2')

    # Tests
    assert get_sum(sample_input1) == 142
    assert get_sum2(sample_input2) == 281

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    question1 = get_sum(puzzle_input)
    question2 = get_sum2(puzzle_input)
    print(f'Q1: {question1}')
    print(f'Q2: {question2}')
