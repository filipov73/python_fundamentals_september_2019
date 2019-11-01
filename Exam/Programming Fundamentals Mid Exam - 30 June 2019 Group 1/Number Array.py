numbers = [int(x) for x in input().split(" ")]

command = input()

while command != "End":
    tokens = command.split(" ")
    if tokens[0] == "Switch":
        idx = int(tokens[1])
        if 0 <= idx < len(numbers):
            numbers[idx] *= -1
    elif tokens[0] == "Change":
        idx = int(tokens[1])
        value = int(tokens[2])
        if 0 <= idx < len(numbers):
            numbers[idx] = value
    elif tokens[0] == "Sum":
        if tokens[1] == "Negative":
            print(sum([x for x in numbers if x < 0]))
        elif tokens[1] == "Positive":
            print(sum([x for x in numbers if x >= 0]))
        elif tokens[1] == "All":
            print(sum(numbers))
# "Switch {index}"
# "Change {index} {value}"
# "Sum Negative"
# "Sum Positive"
# "Sum All"

    command = input()

print(" ".join([str(x) for x in numbers if x >= 0]))
