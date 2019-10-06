cards = input().split(" ")
shuffle = int(input())
middle = int(len(cards) / 2)


for _ in range(shuffle):
    cards = [x for n in zip(cards[:middle], cards[middle:]) for x in n]
print(cards)


# second code

# from itertools import chain
# cards = input().split(" ")
# shuffle = int(input())
# middle = int(len(cards) / 2)
#
#
# for _ in range(shuffle):
#     cards = list(chain(*zip(cards[:middle], cards[middle:])))
# print(cards)
