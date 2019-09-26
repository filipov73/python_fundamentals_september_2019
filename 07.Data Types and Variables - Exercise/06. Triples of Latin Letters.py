from itertools import product

number = int(input())

for n in product(range(97, 97 + number), repeat=3):
    print(''.join(map(chr, n)))
