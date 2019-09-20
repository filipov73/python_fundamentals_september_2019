year = int(input())

while True:
    year += 1
    year_list = list(str(year))
    if len(year_list) == len(set(year_list)):
        print(year)
        break
