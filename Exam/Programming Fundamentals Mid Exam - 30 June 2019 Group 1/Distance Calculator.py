steps = int(input())
length_cm = float(input())
distance_cm = int(input()) * 100

distance = 0
for s in range(1, steps + 1):
    distance += length_cm
    if s % 5 == 0:
        distance -= length_cm * 0.30

percentage = distance / distance_cm * 100
print(f"You travelled {percentage:.2f}% of the distance!")
