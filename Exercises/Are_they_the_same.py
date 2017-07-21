# Are they the "same"?
# 6 kyu

# Given two arrays a and b, write a function comp(array1, array2) that checks
# whether the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in b are the elements in a squared, 
# regardless of the order.

def comp(array1, array2):
    
    # Check that both array1 and array2 are actually lists
    if isinstance(array1, list) and isinstance(array2, list):
    
        # Sort into order
        array1.sort()
        array2.sort()
        
        # Loop over the values in array1, if the square of the value is not 
        # equal to the value in the same index in array 2, return False
        i = 0
        for a1 in array1:
            if not a1**2 == array2[i]:
                return False
            i += 1
        return True
    else:
        return False
