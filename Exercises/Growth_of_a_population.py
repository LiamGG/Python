# Growth of a population
# 7 kyu

# p0 = initial population
# percent = percentage growth of population each year
# aug = net number of citizens that move to the city
# p = target population
# Find how many years it takes to reach p


def nb_year(p0, percent, aug, p):
    # number of year
    n = 0
    # keep running while population < max, add 1 to year for each iteration
    while p0 < p:
        p0 += p0 * percent/100 + aug
        n += 1
    
    return n
