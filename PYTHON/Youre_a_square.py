# You're a square
# 7 kyu

import math

def is_square(num):
    if num < 0: return False
    
    return math.sqrt(num) == int(math.sqrt(num))
