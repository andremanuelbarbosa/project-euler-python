def number_divisors(number):
    divisors = []
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def sum_number_divisors(number):
    divisors = number_divisors(number)
    sum_divisors = 0
    for divisor in divisors:
        sum_divisors += divisor
    return sum_divisors


def solution(max_number):
    amicable_numbers = []
    for i in range(1, max_number):
        a = sum_number_divisors(i)
        b = sum_number_divisors(a)
        if i == b and i != a:
            print(a, b)
            if i not in amicable_numbers:
                amicable_numbers.append(i)
            if a not in amicable_numbers:
                amicable_numbers.append(a)
    sum_amicable_numbers = 0
    for amicable_number in amicable_numbers:
        sum_amicable_numbers += amicable_number
    return sum_amicable_numbers


print(solution(10000))
