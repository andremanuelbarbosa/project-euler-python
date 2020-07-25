def solution(n):
    for _ in range(3000):
        m = -1
        for a in range(3, (n//3)+1):
            b = (n**2 - 2*a*n)//(2*n - 2*a)
            c = n - b - a
            if a**2 + b **2 == c**2:
                if a + b + c == n and a*b*c > m:
                    m = a*b*c
                    return m
    return -1


assert solution(4) == -1
assert solution(12) == 60

print(solution(1000))
