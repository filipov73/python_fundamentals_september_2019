days_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
for d in range(1, days_plunder + 1):
    total_plunder += daily_plunder
    if d % 3 == 0:
        total_plunder += daily_plunder * 0.50
    if d % 5 == 0:
        total_plunder *= (1 - 0.30)

if expected_plunder <= total_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = total_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
