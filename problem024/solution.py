def permute(k, digits, permutations):
    if k == 1:
        permutations.append(digits.copy())
    else:
        permute(k - 1, digits, permutations)
        for i in range(0, k - 1):
            tmp = digits[k - 1]
            if k % 2 == 0:
                digits[k - 1] = digits[i]
                digits[i] = tmp
            else:
                digits[k - 1] = digits[0]
                digits[0] = tmp
            permute(k - 1, digits, permutations)


def lexicographic_permutations(digits):
    permutations = []
    permutations_numbers = []
    permute(len(digits), digits, permutations)
    for permutation in permutations:
        permutations_numbers.append(''.join(str(digit) for digit in permutation))
    permutations_numbers.sort()
    return permutations_numbers


def solution(digits, position):
    return lexicographic_permutations(digits)[position - 1]


assert solution([0, 1, 2], 4) == '120'

print(solution([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000))
