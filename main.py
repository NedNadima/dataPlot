import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [2.525, 2.758, 3.018, 3.322, 3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520, 6.930, 7.349]

plt.plot(years, pops, color=(255/255, 100/255, 100/255))
plt.ylabel("Population in billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.show()