num_1 = float(input())
num_2 = float(input())
num_3 = float(input())

mul = num_1 * num_2 * num_3

if mul == 0:
    print(f"zero")
elif mul > 0:
    print(f"positive")
else:
    print(f"negative")


# mul = [num_1, num_2, num_3]
#
# if mul.count(0) >= 1:
#     print(f"zero")
# else:
#     if mul[0] < 0 or mul[0] < 0:
#         print(f"positive")
#     else:
#         print(f"negative")