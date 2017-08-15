import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980,
         1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4,
        4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9,
          3.0, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]

plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
plt.plot(years, pops, color=(255/255, 100/255, 100/255), marker="o")
plt.plot(years, deaths, '--', color=(0.6, 0.6, 1), marker="+")
plt.title("World Population Growth")
plt.ylabel("Population (billions)")
plt.xlabel("Year")

plt.grid(True)



plt.show()
