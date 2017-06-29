# Stop spinning my words
# 6 kyu

# Reverse the words if it's length is 5 or greater

def spin_words(sentence):
    new = sentence.split(' ')
    i = 0

    for word in new:
        if len(word) < 5:
        	i += 1
        elif len(word) > 4:
            new[i] = word[::-1]
            i += 1

    return " ".join(new)
