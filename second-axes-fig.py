import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,1,4,5]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.text(1, 5, "Wesley Grubbs")
fig.text(0.1, 0.9, "Wesley Grubbs")

plt.show()