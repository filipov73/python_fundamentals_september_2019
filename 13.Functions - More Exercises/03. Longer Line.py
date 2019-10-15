from math import sqrt


def get_distance(x1, y1, x2=0.0, y2=0.0):
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())


line_1_distance = get_distance(x_1, y_1, x_2, y_2)
line_2_distance = get_distance(x_3, y_3, x_4, y_4)

if line_1_distance < line_2_distance:
    point_3_distance = get_distance(x_3, y_3)
    point_4_distance = get_distance(x_4, y_4)
    if point_3_distance > point_4_distance:
        print(f"({int(x_4)}, {int(y_4)})({int(x_3)}, {int(y_3)})")
    else:
        print(f"({int(x_3)}, {int(y_3)})({int(x_4)}, {int(y_4)})")
else:
    point_1_distance = get_distance(x_1, y_1)
    point_2_distance = get_distance(x_2, y_2)
    if point_1_distance > point_2_distance:
        print(f"({int(x_2)}, {int(y_2)})({int(x_1)}, {int(y_1)})")
    else:
        print(f"({int(x_1)}, {int(y_1)})({int(x_2)}, {int(y_2)})")
