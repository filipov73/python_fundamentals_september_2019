numbers = list(map(int, input().split(", ")))
beggars = int(input())
beggar_list = [x * 0 for x in range(beggars)]
# beggar_list = [0] * beggars
idx = 0

for i in range(len(numbers)):
    beggar_list[idx] += numbers[i]
    if idx == beggars - 1:
        idx = 0
        continue
    idx += 1
print(beggar_list)

