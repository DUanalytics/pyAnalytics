#Topic: Zipf Distribution
#Ex Project -2 
#-----------------------------
import numpy as np
objlist = ['Here', 'in', 'the', 'wall', 'why']
index = np.random.zipf([1.2, 1.2])
index
for idx in index:
    if idx < len(objlist):
        print(objlist[idx])
    else: 
        print "Index {} exceed list".format(idx)