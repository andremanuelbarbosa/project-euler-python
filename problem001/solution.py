def solution(n):
    terms3 = int((n - 1) / 3)
    sum3 = (terms3 * (2 * 3 + (terms3 - 1) * 3)) // 2
    terms5 = int((n - 1) / 5)
    sum5 = (terms5 * (2 * 5 + (terms5 - 1) * 5)) // 2
    terms15 = int((n - 1) / 15)
    sum15 = (terms15 * (2 * 15 + (terms15 - 1) * 15)) // 2
    return sum3 + sum5 - sum15


assert solution(1) == 0
assert solution(10) == 23
assert solution(20) == 78
assert solution(31) == 225
assert solution(100) == 2318

print(solution(1000))
