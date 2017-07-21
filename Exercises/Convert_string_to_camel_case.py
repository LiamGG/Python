# Convert string to camel case
# 5 kyu

# Write a method/function so that converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized.

def to_camel_case(text):
    # Replace all _ with -, split string into array at -
    words = text.replace('_','-').split('-')
    
    # Final array, first word is same case as before
    camelCase = [words[0], ]
    
    # For subsequent words, capitalize the first letter with .title()
    for word in words[1:]:
        camelCase.append(word.title())
        
    return ''.join(camelCase)
    
