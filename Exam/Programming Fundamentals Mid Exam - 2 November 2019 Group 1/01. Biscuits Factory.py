from math import floor
biscuits = int(input())
workers = int(input())
other_factory_per_30 = int(input())

products = 0

for d in range(1, 30 + 1):
    if d % 3 == 0:
        products += floor(biscuits * workers * 0.75)
    else:
        products += (biscuits * workers)


print(f"You have produced {products} biscuits for the past month.")

percentage = (products - other_factory_per_30) / other_factory_per_30 * 100

if products > other_factory_per_30:
    print(f"You produce {abs(percentage):.2f} percent more biscuits.")
else:
    print(f"You produce {abs(percentage):.2f} percent less biscuits.")

