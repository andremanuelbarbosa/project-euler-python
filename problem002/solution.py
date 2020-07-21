def solution(n):
    fibonacci_sum = 0
    fibonacci_current = 2
    fibonacci_previous = 1
    while fibonacci_current < n:
        fibonacci_next = fibonacci_current + fibonacci_previous
        fibonacci_previous = fibonacci_current
        if fibonacci_current % 2 == 0:
            fibonacci_sum += fibonacci_current
        fibonacci_current = fibonacci_next
    return fibonacci_sum


assert solution(10) == 10
assert solution(100) == 44

print(solution(4000000))
