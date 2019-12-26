# A number is called Perfect Number,
# if it's equal to the sum of it's proper
# positive divisor excluding the number itself
# E.g., 6 is a Perfect Number (1+2+3=6)


def perfect_number(num):
    factors = list()
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    if sum(factors) == num:
        print(num, 'is a Perfect Number!')
    else:
        print(num, 'is not a Perfect Number!')


num = 496
perfect_number(num)