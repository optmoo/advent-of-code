import sys

def main():
    total = 0
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            total += 1
    print('Sum:', total)

if __name__ == '__main__':
    main()
