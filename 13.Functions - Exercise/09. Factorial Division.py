def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num_1 = int(input())
num_2 = int(input())

res_1 = factorial(num_1)
res_2 = factorial(num_2)
print(f"{res_1 / res_2:.2f}")
