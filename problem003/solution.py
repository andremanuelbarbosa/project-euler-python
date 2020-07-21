import math


def solution(n):
    factor = 2
    while factor <= math.floor(math.sqrt(n)):
        if n % factor == 0:
            n /= factor
        else:
            factor += 1
    return int(n)


assert solution(10) == 5
assert solution(17) == 17
assert solution(13195) == 29

print(solution(600851475143))
