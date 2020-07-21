def is_divisible(number, n):
    for i in range(1, n + 1):
        if number % i != 0:
            return False
    return True


def solution(n):
    number = n
    while not is_divisible(number, n):
        number += n
    return number


assert solution(3) == 6
assert solution(10) == 2520

print(solution(20))
