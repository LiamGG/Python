# Convert string to camel case
# 5 kyu

def to_camel_case(text):
    # Replace all _ with -, split string into array at -
    words = text.replace('_','-').split('-')
    
    # Final array, first word is same case as before
    camelCase = [words[0], ]
    
    # For subsequent words, capitalize the first letter with .title()
    for word in words[1:]:
        camelCase.append(word.title())
        
    return ''.join(camelCase)
    
