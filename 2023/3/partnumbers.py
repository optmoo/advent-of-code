import numpy as np
import re
import sys

def main():
    total = 0
    gear_ratios = 0
    symbols ='&/*%+$-@#='
    digit_pattern = re.compile('\d+')
    gear_pattern = re.compile('\*')

    with open(sys.argv[1], 'rt') as f:
        lines = list(map(lambda l: list(l.strip()), f.readlines()))
        old_schematic = np.array(lines)
        schematic = np.array(lines)
        row, col = schematic.shape
        valid = np.array([[False for _ in range(col)] for _ in range(row)])
        touch_gear = np.array([[False for _ in range(col)] for _ in range(row)])

        # mark all cells that touch a "symbol"
        for r in range(row):
            for c in range(col):
                if schematic[r][c] == '*':
                    touch_gear[r+1][c+1] = True
                    touch_gear[r+1][c  ] = True
                    touch_gear[r+1][c-1] = True
                    touch_gear[r  ][c+1] = True
                    touch_gear[r  ][c-1] = True
                    touch_gear[r-1][c+1] = True
                    touch_gear[r-1][c  ] = True
                    touch_gear[r-1][c-1] = True
                if schematic[r][c] in symbols:
                    valid[r+1][c+1] = True
                    valid[r+1][c  ] = True
                    valid[r+1][c-1] = True
                    valid[r  ][c+1] = True
                    schematic[r][c] = '.'
                    valid[r  ][c-1] = True
                    valid[r-1][c+1] = True
                    valid[r-1][c  ] = True
                    valid[r-1][c-1] = True
        
        # extract all numbers
        for r in range(row):
            line = ''.join(schematic[r])
            for num in digit_pattern.finditer(line):
                # if any of it's cells are valid
                s, e = num.span()
                if any(valid[r][s:e]):
                    total += int(num.group())

        # extract all gears
        for r in range(1, row-1): # skipping first and last rows to avoid boundary condition ... valid for input
            line = ''.join(old_schematic[r])
            for gear in gear_pattern.finditer(line):
                gears = []
                gear_s, gear_e = gear.span()

                for num in digit_pattern.finditer(''.join(old_schematic[r-1])): # row above
                    s, e = num.span()
                    if any(touch_gear[r-1][s:e]) and (gear_s <= e and s <= gear_e):
                        gears.append(int(num.group()))
                for num in digit_pattern.finditer(''.join(old_schematic[r])): # row
                    s, e = num.span()
                    if any(touch_gear[r][s:e]) and (gear_s <= e and s <= gear_e):
                        gears.append(int(num.group()))
                for num in digit_pattern.finditer(''.join(old_schematic[r+1])): # row below
                    s, e = num.span()
                    if any(touch_gear[r+1][s:e]) and (gear_s <= e and s <= gear_e):
                        gears.append(int(num.group()))

                if len(gears) == 2:
                    gear_ratios += gears[0] * gears[1]
            
    print("Sum of part numbers:", total)
    print("Sum of gear ratios:", gear_ratios)
    # Sum of part numbers: 517021
    # Sum of gear ratios: 81296995


if __name__ == '__main__':
    main()
