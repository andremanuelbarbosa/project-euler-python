def factorial(number):
    number_factorial = 1
    for i in range(2, number + 1):
        number_factorial *= i
    return number_factorial


def sum_digits(number):
    digits_sum = 0
    number_str = str(number)
    for i in range(0, len(number_str)):
        digits_sum += int(number_str[i])
    return digits_sum


def solution(number):
    return sum_digits(factorial(number))


assert solution(10) == 27

print(solution(100))
