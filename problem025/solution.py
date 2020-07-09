fibonaccis = {}


def fibonacci(number):
    if number in fibonaccis:
        return fibonaccis[number]
    else:
        if number == 1 or number == 2:
            return 1
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)


def solution(digits_count):
    number = 0
    number_fibonacci = 0
    while len(str(number_fibonacci)) < digits_count:
        number += 1
        number_fibonacci = fibonacci(++number)
        fibonaccis[number] = number_fibonacci
    return number


assert solution(3) == 12

print(solution(1000))
