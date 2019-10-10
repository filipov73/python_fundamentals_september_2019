numbers = input().split(", ")

z_list = [numbers.remove(x) for x in numbers if x == "0"]
for _ in range(len(z_list)):
    numbers.append("0")
c = list(filter(lambda x: x != "0", numbers))
a = list(map(int, numbers))
print(a)

a=5
# numbers = list(map(int, input().split(", ")))
# zero_list = []
# i = 0
#
# while 0 in numbers:
#     if numbers[i] == 0:
#         numbers.pop(i)
#         zero_list.append(0)
#     i += 1
# numbers += zero_list
# print(numbers)
#
# elements = input().split(", ")
# zeros_count = len(list(filter(lambda x: x == "0", elements)))
# filtered_elements = list(map(lambda y: int(y), list(filter(lambda x: x != "0", elements))))
# for x in range(zeros_count):
#     filtered_elements.append(0)
# print(filtered_elements)