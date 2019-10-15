from math import sqrt


def get_distance(x, y):
    distance = sqrt((x - 0)**2 + (y - 0)**2)
    return distance


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

point_1_distance = get_distance(x_1, y_1)
point_2_distance = get_distance(x_2, y_2)

if point_1_distance > point_2_distance:
    print(f"({int(x_2)}, {int(y_2)})")
else:
    print(f"({int(x_1)}, {int(y_1)})")
