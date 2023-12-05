import sys

def parse_game(line):
    game = int(line[line.index(' '):line.index(':')])
    draws = line[line.index(':')+2:].split( '; ')
    # print('game', game, draws)

    ret = True
    max_cubes = {'red':0, 'green':0, 'blue':0}
    for draw in draws:
        cubes = {'red':0, 'green':0, 'blue':0}
        for cube in draw.split(', '):
            num, color = cube.split(' ')
            cubes[color] = int(num)
            if max_cubes[color] < int(num):
                max_cubes[color] = int(num)

        if cubes['red'] > 12:
            ret = False
        if cubes['green'] > 13:
            ret = False
        if cubes['blue'] > 14:
            ret = False

    power = max_cubes['red'] * max_cubes['green'] * max_cubes['blue']

    return game, ret, power

def main():
    total = 0
    total_power = 0
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            game, possible, power = parse_game(line.strip())
            total += game if possible else 0
            total_power += power
    print('Sum:', total)
    print('Power:', total_power)


if __name__ == '__main__':
    main()
