# Which are in?
# 6 kyu

def in_array(array1, array2):
    a = len(array1)
    b = len(array2)
    results = []
    
    for i in range(a):
        for j in range(b):
            if array1[i] in array2[j]:
                results.append(array1[i])
    
    return sorted(set(results))
