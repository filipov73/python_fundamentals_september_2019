print("\n".join(map(lambda x: x*"*", [n if n <= num else num*2 - n for num in [int(input())] for n in range(1, num*2)])))
