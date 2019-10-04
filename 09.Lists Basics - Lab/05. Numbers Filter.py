num = int(input())

numbers_list = []
filtered_list = []
commands_dict = {
    'even': 'x % 2 == 0',
    'odd': 'x % 2 == 1',
    'positive': 'x >= 0',
    'negative': 'x < 0'
}
for _ in range(num):
    number = int(input())
    numbers_list.append(number)
command = input()
if command in commands_dict.keys():
    filtered_list = list(filter(lambda x: eval(commands_dict[command]), numbers_list))
print(filtered_list)
