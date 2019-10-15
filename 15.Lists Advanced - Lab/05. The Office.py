happiness_list = list(map(int, input().split(" ")))
happiness_percent = int(input())
happiness_list_with_percent = [x * happiness_percent for x in happiness_list]
average_happiness = sum(happiness_list_with_percent) / len(happiness_list_with_percent)
filtered_happiness_list = list(filter(lambda x: x >= average_happiness, happiness_list_with_percent))
if len(happiness_list) / 2 > len(filtered_happiness_list):
    print(f"Score: {len(filtered_happiness_list)}/{len(happiness_list)}. Employees are not happy!")
else:
    print(f"Score: {len(filtered_happiness_list)}/{len(happiness_list)}. Employees are happy!")
