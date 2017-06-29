# Find the divisors
# 7 kyu 

#Find the divisors of an input integer

def divisors(integer):
    # create array of numbers to test
    test = list(range(2, int(integer/2) + 1))
    divisors = []

    # for each number in the range, if remaineder = 0 it's a divisor, append to list
    for x in test:
        if integer % x == 0:
            divisors.append(x)

    # if there are no divisors from the range, the number is prime
    if len(divisors) == 0:
        return (str(integer) + ' is prime')
    else:
        return divisors
