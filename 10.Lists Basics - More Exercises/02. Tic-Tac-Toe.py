import numpy

line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")

matrix = [
    line_1,
    line_2,
    line_3
]

print(*map(int, matrix))
