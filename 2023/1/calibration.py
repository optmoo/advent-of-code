import sys

def replace_num_words_LR(line):
    digit_map = {'one':'1e', 'two':'2', 'three':'3e', 'four':'4', 'five':'5e', 
                 'six':'6', 'seven':'7n', 'eight':'8', 'nine':'9e'}

    start = end = 0
    new_line = line
    while start < len(line):
        token = line[start:end+1]
        if token in digit_map.keys():
            print('found', token)
            new_line = new_line.replace(token,digit_map[token], 1)
            start = end = start+1
        elif end - start == 5:
            # print('skipping', token)
            start = end = start+1
        else:
            end += 1
    # print(line[start:end+1], start, end)
    for word in digit_map.keys():
        if word in new_line:
            print('!!', new_line)
    return new_line

def find_digits(line):
    digit_map = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
                 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    start = end = 0
    digits = ''
    while start < len(line):
        token = line[start:end+1]
        if token.isdigit():
            digits += token
            start = end = start+1
            continue

        if token in digit_map.keys():
            print('found', token)
            digits += digit_map[token]
            start = end = start+1
        elif end - start == 5:
            # print('skipping', token)
            start = end = start+1
        else:
            end += 1
    # print(line[start:end+1], start, end)
    return digits

words = ['oneightwoneight']

def main():
    total = 0
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            digits = find_digits(line.strip())
            # digits = list(filter(lambda c: c.isdigit(), new_line))
            print(line.strip(), digits, digits[0] + digits[-1])
            total += int(digits[0] + digits[-1])
    print('Sum:', total)

if __name__ == '__main__':
    main()
    print(find_digits(words[0]))
