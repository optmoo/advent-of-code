import sys

def main():
    total = 0
    original = []
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            card_num, numbers = line.strip().split(':')
            card_id = int(card_num.split()[1])
            card, winning = numbers.split('|')

            n_card = set(card.split(' '))
            n_winning = set(winning.split(' '))


            winners = n_card.intersection(n_winning)
            winners.remove('')
            
            original.append((card_id, len(winners)))

            if len(winners) > 0:
                total += 2**(len(winners)-1)
    print('Total points:', total)

    scratchers = [1 for _ in original]
    for card_id, winners in original:
        for i in range(card_id, card_id+winners):
            scratchers[i] += scratchers[card_id-1]
    print('Total scratchers:', sum(scratchers))

if __name__ == '__main__':
    main()
