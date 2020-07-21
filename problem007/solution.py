import math


max_number = 105000
are_primes = []
for i in range(0, max_number):
    are_primes.append(True)
for i in range(2, math.ceil(math.sqrt(max_number))):
    if are_primes[i - 1]:
        for j in range(i * i, max_number + 1, i):
            are_primes[j - 1] = False
primes = []
for i in range(1, max_number):
    if are_primes[i]:
        primes.append(i + 1)


def solution(n):
    return primes[n - 1]


assert solution(3) == 5
assert solution(6) == 13
assert solution(10) == 29

print(solution(10001))
