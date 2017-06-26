# Simple Pig Latin
# 5 kyu

def pig_it(text):
    pyg = 'ay'
    
    words = text.split(' ')

    i = 0
    for word in words:
        if word.isalpha():
            new_word = word + word[0] + pyg
            new_word = new_word[1:len(new_word)]
            words[i] = new_word
        else:
            words[i] = word
        i += 1
    return ' '.join(words)
