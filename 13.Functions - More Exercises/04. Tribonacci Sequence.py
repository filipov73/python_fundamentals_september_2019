def tribonacci_sequence(num):
    n1 = 0
    n2 = 0
    n3 = 1
    seq = [n3]
    for _ in range(num - 1):
        n1, n2, n3 = n2, n3, n1+n2+n3
        seq.append(n3)
    return seq


num = int(input())
print(" ".join(list(map(str, tribonacci_sequence(num)))))


# def tribonacci_sequence(num):
#     # seq = []
#     if num == 0 or num == 1 or num == 2:
#         return 0
#     if num == 3:
#         return 1
#     else:
#         return tribonacci_sequence(num - 3) + tribonacci_sequence(num - 2) + tribonacci_sequence(num - 1)
#
# num = int(input())
#
# seq = []
# for n in range(1, num + 1):
#     seq.append(tribonacci_sequence(n))
# print(" ".join(list(map(str, seq))))
