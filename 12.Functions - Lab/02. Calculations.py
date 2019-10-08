import operator

operators_dict = {
        'multiply': operator.mul,
        'divide': operator.truediv,
        'add': operator.add,
        'subtract': operator.sub
}


def calculator(op, num_1, num_2):
    return f"{int(operators_dict[op](num_1, num_2))}"


operator = input()
first_num = int(input())
second_num = int(input())

print(calculator(operator, first_num, second_num))
