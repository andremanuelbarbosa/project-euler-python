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
    abundant_numbers = []
    for i in range(12, max_number):
        if sum_number_divisors(i) > i:
            abundant_numbers.append(i)
    non_abundant_numbers = []
    for i in range(0, max_number + 1):
        non_abundant_numbers.append(i)
    for i in abundant_numbers:
        for j in abundant_numbers:
            sum_abundant_numbers = i + j
            if sum_abundant_numbers <= max_number:
                non_abundant_numbers[sum_abundant_numbers] = 0;
    sum_non_abundant_numbers = 0
    for i in non_abundant_numbers:
        sum_non_abundant_numbers += i
    return sum_non_abundant_numbers


print(solution(28123))
