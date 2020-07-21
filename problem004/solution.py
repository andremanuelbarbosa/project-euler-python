def is_palindromic(n):
    n1 = str(n)
    n2 = ""
    for i in range(len(n1), 0, -1):
        n2 += n1[i - 1]
    return n1 == n2


def solution(n, max):
    max_number = pow(10, n) - 1
    largest_palindrome = 0
    for i in range(max_number, 0, -1):
        for j in range(max_number, i - 1, -1):
            number = i * j
            if (not max or number < max) and number >= largest_palindrome and is_palindromic(number):
                largest_palindrome = number
    return largest_palindrome


assert solution(2, None) == 9009
assert solution(3, 101110) == 101101
assert solution(3, 800000) == 793397

print(solution(3, None))
