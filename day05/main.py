# Day 5, If You Give A Seed A Fertilizer

# Q1

# Q2

# Input
def map_parse(m):
    name = m[0][:-5].split('-')
    fr = name[0]
    to = name[2]
    nums = [ for . in m[1:]]

def parse_input(file):
    maps = {}
    with open(file, 'r') as inp:
        raw = [g for g in inp.read().split('\n\n') if g]
        seeds = [int(s) for s in raw[0].split()[1:]]
        _maps = [m.split('\n') for m in raw[1:]]
        
            

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = 0
    t2 = 0
    assert t1 == 0, t1
    assert t2 == 0, t2

    # Puzzle input
    #puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = 0
    q2 = 0
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
