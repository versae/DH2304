import numpy as np


data = np.loadtxt('data/populations.txt')
year, hares, lynxes, carrots = data.T
species = np.array(['Hare', 'Lynx', 'Carrot'])

# we first create an array with the populations
populations = data[:,1:]

# 1
print("\t", "\t\t".join(species))
means = populations.mean(axis=0)
print("Mean:", means)
stds = populations.std(axis=0)
print("Std:", stds)

# 2
species_max_year = np.argmax(populations, axis=0)
max_years = year[species_max_year]
print("\t    ", "   ".join(species))
print("Max. year:", max_years)

# 3
max_species = np.argmax(populations, axis=1)
print("Max species:")
print(year)
print(species[max_species])

# 4
above_50k = np.any(populations > 50000, axis=1)
year_above_50k = year[above_50k]
print("Any above 50000:", year_above_50k)

# 5
top_2 = np.argsort(populations, axis=0)[:2]
print("Top 2 years with lowest populations for each:")
print("  ", "   ".join(species))
print(year[top_2])
