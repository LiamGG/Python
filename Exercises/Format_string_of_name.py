# Format a string of names
# 6 kyu

# Given: an array containing hashes of names
# Return: a string formatted as a list of names separated by commas 
# except for the last two names, which should be separated by an ampersand.

def namelist(names):
    arr = []
    for name in names:
        arr.append(name['name'])
    
    if len(arr) == 1:
        return arr[0]
    elif len(arr) > 1:
        return ', '.join(arr[:-1]) + " & " + arr[len(arr)-1]
    else:
        return ''
    
