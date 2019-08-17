# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
data = np.arange(3000).reshape((100,30))
plt.imshow(data)
#plt.savefig('test.png', bbox_inches='tight')

#
import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(0, 1, 20); ys = np.sin(xs)

fig = plt.figure()
axes = fig.add_subplot(1,1,1)
axes.plot(xs, ys)
# This should be called after all axes have been added
fig.tight_layout()
#fig.savefig('test.png')


#!----------------

import matplotlib.pyplot as plt
data=np.arange(3000).reshape((100,30))
plt.plot(data)
plt.subplots_adjust(left=.1, right=0.9, top=0.9, bottom=.1)

plt.plot(data)
plt.subplots_adjust(left=.2, right=0.9, top=0.9, bottom=.1)

plt.plot(data)
plt.subplots_adjust(left=.3, right=0.8, top=0.8, bottom=.3)


# Let's consider a basic barplot.
import matplotlib.pyplot as plt
#margins(margin)
import numpy as np
y_pos = np.arange(len(bars))
bars = ('A','B','C','D','E')
height = [3, 12, 5, 18, 45]
plt.bar(y_pos, height)
 
# If we have long labels, we cannot see it properly
names = ("very long group name 1","very long group name 2","very long group name 3","very long group name 4","very long group name 5")
plt.xticks(y_pos, names, rotation=90)
 
# Thus we have to give more margin:
plt.subplots_adjust(bottom=0.4)
 
# It's the same concept if you need more space for your titles
plt.title("This is\na very very\nloooooong\ntitle!")
plt.subplots_adjust(top=0.7)
