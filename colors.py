import matplotlib.pyplot as plt
from pypalettes import load_cmap

cmap = load_cmap("Acadia")
colors = cmap.colors

year = [2010, 2011, 2012, 2013]
y1 = [3, 4, 2, 5]
y2 = [1, 5, 3, 2]
y3 = [8, 2, 4, 6]
y4 = [8, 12, 4, 1]

fig, ax = plt.subplots()
ax.stackplot(year, y1, y2, y3, y4, colors=colors)
plt.show()