# Find the next perfect square
# 7 kyu


#if the input number is a perfect square, find the next perfect square

import math

def find_next_square(sq):
    # if square root of the number is an integer
    # add one to the sqaure root, and square
    if (math.sqrt(sq)).is_integer():
        return ((math.sqrt(sq)) + 1) **2
        
    #else if not a perfect square, return -1 as required
    else:
        return -1
