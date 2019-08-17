#
#-----------------------------
#%
import matplotlib.pyplot as plt

# simulating a pandas df['type'] column
types = ['apple', 'orange', 'apple', 'pear', 'apple', 'orange', 'apple', 'pear']
x_coords = [10, 10, 5, 4, 3, 20, 19, 21]
y_coords = [21, 23, 12, 21, 10, 20, 14, 2]

for i, type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='x', color='red')
    plt.text(x+0.3, y+0.3, type, fontsize=9)
plt.show()


#------
