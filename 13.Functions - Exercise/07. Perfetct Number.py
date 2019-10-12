def aliquot_sum(num):
    sums = 0
    for n in range(1, num):
        if num % n == 0:
            sums += n
    return sums


number = int(input())
res = aliquot_sum(number)
if number == res:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
