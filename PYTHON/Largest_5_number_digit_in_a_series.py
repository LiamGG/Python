# Largest 5 number digit in a series
# 5 kyu

def solution(digits):
    digits = str(digits)
    value = 0
    i = 0
    for digit in digits:
        test = int("".join(digits[i:i+5]))
        if test > value:
            value = test
        i += 1

    return value
