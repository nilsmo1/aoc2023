# Day 3, Gear Ratios

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
def gear_cond(c):
    return c.isdigit()

def get_nums(r, c, schema):
    #print("found", r, c)
    ids = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    connections = [(r+rr, c+cc) for cc, rr in ids if
                   in_bounds(r+rr, c+cc, schema) and
                   schema[r+rr][c+cc].isdigit()]
    #print("connections", connections)
    nums = []
    invalids = []
    for i, (row, col) in enumerate(connections[:-1]):
        r2, c2 = connections[i+1]
        if row == r2 and abs(col - c2) == 1:
            invalids.append(i)

    for i, (row, col) in enumerate(connections):
        if i in invalids: continue
        start, end = col, col
        #print(f"{schema[row][end]} at {start}, {end}, {row=}")
        while schema[row][end].isdigit() and end + 1 < len(schema[row]):
            #print(schema[row][end])
            end += 1
        while schema[row][start-1].isdigit() and start > 0:
            start -= 1
        substring = schema[row][start:end]
        #print(substring, start, end)
        nums.append(int(substring))
    if len(nums) != 2: return 0
    n1, n2 = nums
    return n1 * n2

def gear_ratio(schema):
    products = []
    for row, r in enumerate(schema):
        for col, c in enumerate(r):
            if c == '*' and symbol_neighbour(row, col, schema, gear_cond) > 1:
                products.append(get_nums(row, col, schema))
                #print(c, products)
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
