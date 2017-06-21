# Isograms
# 7kyu

# Determine if a word is an isogram (has a repeating letter)

def is_isogram(string):
    # ignore case by setting all to lower case
    string = string.lower()
    
    # iterate over each character, if there's more than 1, return False
    for letter in string:
        if string.count(letter) > 1:
            return False
            
    # otherwise return True
    return True
