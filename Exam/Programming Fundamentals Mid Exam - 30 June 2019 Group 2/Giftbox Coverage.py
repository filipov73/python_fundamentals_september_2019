size = float(input())
number = int(input())
area = float(input())

area_box = (size * size) * 6

area_papers = 0
for n in range(1, number + 1):
    if n % 3 == 0:
        area_papers += area * 0.25
    else:
        area_papers += area


percentage = area_papers / area_box * 100
print(f"You can cover {percentage:.2f}% of the box.")
