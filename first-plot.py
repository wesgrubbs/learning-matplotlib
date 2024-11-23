import matplotlib.pyplot as plt # Create an empty canva that contains all elements of the graph

# All the code that draws teh visual elements: lines, points, maps, title, legend, etc. goes here
x = [1,2,3,4,5]
y = [2,3,1,4,5]

fig, ax = plt.subplots()
#ax.plot([x, y)
ax.scatter(x, y)

# Finally, we display the graph
plt.show()