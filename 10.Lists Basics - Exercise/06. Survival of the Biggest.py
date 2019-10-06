integer_list = list(map(int, input().split(" ")))
number = int(input())

for _ in range(number):
    min_num = min(integer_list)
    integer_list.pop(integer_list.index(min_num))
print(integer_list)
