def max_number(numbers):
    if not numbers:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    else:
        return max(numbers[0], max_number(numbers[1:]))

# [2, 4, 45, 56, 23, 4]
