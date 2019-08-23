#Stack Plot: Cumumulative Sum #Combined Dept
#-----------------------------
import numpy as np
import matplotlib.pyplot as plt
#
rng = np.arange(50)
rng.size
#50 data for each country between 0 and 10
rnd = np.random.randint(0, 10, size=(3, rng.size))
rnd
#from 1950 to next 50 yrs
yrs = 1950 + rng
yrs
#plot
fig, ax = plt.subplots(figsize=(5, 3))
#rng + rnd : cumulative sum
ax.stackplot(yrs, rng + rnd, labels=['India', 'Pakistan', 'Bangladesh'])
ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()
plt.show();