def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n + 1):
        sum_squares += i * i;
    return sum_squares


def square_of_sums(n):
    squares_sum = 0
    for i in range(1, n + 1):
        squares_sum += i
    return squares_sum * squares_sum


def solution(n):
    return square_of_sums(n) - sum_of_squares(n)


assert solution(3) == 22
assert solution(10) == 2640

print(solution(100))
