# Persistent bugger
# 6 kyu

# Return a number's multiplicative persistence

def persistence(num):

    if len(str(num)) == 1: return 0
    
    count = 0

    while len(str(num)) > 1:
        y=1
        arr = [int(digit) for digit in str(num)]
        for x in arr:
            y *= x
            num = y
            
        count += 1
    
    return count
