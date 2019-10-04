num = int(input())

positives_list = []
negatives_list = []

for _ in range(num):
    number = int(input())
    if number >= 0:
        positives_list.append(number)
    else:
        negatives_list.append(number)
count_positives = len(positives_list)
sum_of_negatives = sum(negatives_list)
print(positives_list)
print(negatives_list)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")
