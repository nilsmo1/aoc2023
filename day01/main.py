# Day 1, Trebuchet?!
from typing import List


# Q1
def get_sum(doc: List[str]) -> int:
    nums = [[c for c in line if c.isdigit()] for line in doc]
    return sum(int(ds[0] + ds[-1]) for ds in nums)


# Q2
def get_sum2(doc: List[str]) -> int:
    nums = []
    digits = ["one", "two",   "three", "four", "five",
              "six", "seven", "eight", "nine"]
    for line in doc:
        sub_nums = []
        for i, c in enumerate(line):
            if c.isdigit():
                sub_nums.append(c)
                continue
            for val, d in enumerate(digits):
                if line[i:].startswith(d):
                    sub_nums.append(str(val+1))
                    break
        nums.append(sub_nums)
    return sum(int(ds[0]+ds[-1]) for ds in nums)


# Input
def parse_input(file):
    with open(file, 'r') as inp:
        return [line.strip() for line in inp.readlines()]


if __name__ == '__main__':
    # Samples
    sample_input1 = parse_input('sample1')
    sample_input2 = parse_input('sample2')

    # Tests
    assert get_sum(sample_input1)  == 142
    assert get_sum2(sample_input2) == 281

    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    question1 = get_sum(puzzle_input)
    question2 = get_sum2(puzzle_input)
    print(f'Q1: {question1}')
    print(f'Q2: {question2}')
