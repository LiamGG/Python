# Remove the minimum
# 7 kyu

# Remove the smallest value from the input array, without sorting the array.
# Only remove the first instance of the number


def remove_smallest(numbers):
    
    # if the array is empty, return the empty array
    if len(numbers) < 1:
        return numbers
        
    # else remove the minimum value by:
    # finding minimum number using min(numbers)
    # removing using .remove(), which stops after removing the first instance
    else:
        numbers.remove(min(numbers))
        return numbers
    
