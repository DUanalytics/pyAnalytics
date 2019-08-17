#Fill Between
#-----------------------------
#%
#https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/fill_between_demo.html
fig, ax = plt.subplots()
y = np.sin(4 * np.pi * x)
ax.plot(x, y, color='black')

# use data coordinates for the x-axis and the axes coordinates for the y-axis
import matplotlib.transforms as mtransforms
trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
theta = 0.9
ax.axhline(theta, color='green', lw=2, alpha=0.5)
ax.axhline(-theta, color='red', lw=2, alpha=0.5)
ax.fill_between(x, 0, 1, where=y > theta,  facecolor='green', alpha=0.5, transform=trans)
ax.fill_between(x, 0, 1, where=y < -theta, facecolor='red', alpha=0.5, transform=trans)


plt.show()