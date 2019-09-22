word = input()
result = []

for i in range(len(word)):
  if word[i].isupper():
    result.append(i)
print(result)