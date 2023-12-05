# Day 2, Cube Conundrum

# Q1
def get_sum_games(games):
    colors = {'red': 12, 'green': 13, 'blue': 14}
    game_sum = 0
    for nr, game in games.items():
        for sack in game:
            valid = True
            for item in sack:
                for c in colors:
                    n = int(item.strip().split()[0])
                    if c in item and n > colors[c]:
                        valid = False
                        break
            if not valid: break
        game_sum += nr if valid else 0
    return game_sum


# Q2
def get_power_game(games):
    game_sum = 0
    for nr, g in games.items():
        colors = {'red': 0, 'green': 0, 'blue': 0}
        for s in g:
            for item in s:
                n = int(item.strip().split()[0])
                for c in colors:
                    if c in item: colors[c] = max(n, colors[c])
        r, g, b = colors.values()
        game_sum += r * g * b
    return game_sum

# Input
def parse_input(file):
    with open(file, 'r') as inp:
        RAW = inp.readlines()
    games = {}
    for i, game in enumerate(RAW):
        games[i+1] = [line.split(',') for line in game.split(':')[1:][0].split(';')]
    return games

if __name__ == '__main__':
    # Samples
    sample_input = parse_input('sample')

    # Tests
    t1 = get_sum_games(sample_input)
    t2 = get_power_game(sample_input)
    assert t1 == 8, t1
    assert t2 == 2286, t2


    # Puzzle input
    puzzle_input = parse_input('puzzle-input')

    # Results
    q1 = get_sum_games(puzzle_input)
    q2 = get_power_game(puzzle_input)
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
