import numpy as np

line_1 = list(map(int, input().split(" ")))
line_2 = list(map(int, input().split(" ")))
line_3 = list(map(int, input().split(" ")))

matrix = np.array([
    line_1,
    line_2,
    line_3
])
winner = None
for i in range(3):
    if len(set(matrix[:, i])) == 1:
        winner = list(set(matrix[:, i]))[0]
        break
    elif len(set(matrix[i, :])) == 1:
        winner = list(set(matrix[i, :]))[0]
        break

if len(set(matrix.diagonal())) == 1:
    winner = list(set(matrix.diagonal()))[0]
elif len(set(np.fliplr(matrix).diagonal())) == 1:
    winner = list(set(np.fliplr(matrix).diagonal()))[0]
if winner is not None:
    if winner == 1:
        print("First player won")
    else:
        print("Second player won")


