# Square every digit
# 7 kyu

def square_digits(num):
    # create an array of the digits in the number
    digits = [int(digit) for digit in str(num)]
    
    # square each nunber in the array
    digits_sq = [(x**2) for x in digits]
    
    # return by converting to string, joining, and converting total to integer
    total = ''.join(map(str, digits_sq))
    return int(total)
