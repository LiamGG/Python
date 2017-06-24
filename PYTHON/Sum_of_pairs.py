# Sum of pairs
# 5 kyu

# Given a list of integers and a single sum value, 
# return the first two values (parse from the left please) in order of 
# appearance that add up to form the sum.

def sum_pairs(ints, s):
	x = len(ints)
	y = []
    
    # Python 2.x -> xrange(), Python 3.x -> range()
	for i in xrange(x):
		if s - ints[i] in y:
			return [s - ints[i], ints[i]]
		if not ints[i] in y:
			y.append(ints[i])
	return None
