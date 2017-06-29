# Weight for weight
# 6 kyu

# Attribute a "weight" to numbers.
# The weight of a number will be from now on the sum of its digits.
# For example 99 will have "weight" 18, 100 will have "weight" 1 so
# in the list 100 will come before 99. Given a string with the weights 
# of FFC members in normal order can you give this string ordered by 
# "weights" of these numbers?

def sums(string):
    return sum( [int(num) for num in string] )

def compare(a, b):
    if sums(a) == sums(b):
        if a < b:
            return -1
        return 1
    elif sums(a) > sums(b):
        return 1
    return -1
    
def order_weight(strng):
    nums = strng.split(" ")

    nums.sort(compare);
    return " ".join(nums)

