import math


max_number = pow(10, 7)
are_primes = []
for i in range(0, max_number):
    are_primes.append(True)
for i in range(2, math.ceil(math.sqrt(max_number))):
    if are_primes[i - 1]:
        for j in range(i * i, max_number + 1, i):
            are_primes[j - 1] = False
sums_primes = []
for i in range(0, max_number):
    sums_primes.append(0 if i == 0 else sums_primes[i - 1] + (i + 1) if are_primes[i] else sums_primes[i - 1])


def solution(n):
    return sums_primes[n - 1]


assert solution(5) == 10
assert solution(10) == 17

print(solution(2000000))
