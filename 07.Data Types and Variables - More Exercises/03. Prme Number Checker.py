number = int(input())
checker = None

if number > 1:
    for n in range(2, number):
        if number % n == 0:
            checker = False
            break
        else:
            checker = True
else:
    checker = False
print(checker)
