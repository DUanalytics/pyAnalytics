#Bar Plot
#-----------------------------
#%
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig, ax = plt.subplots(nrows=1, ncols=1)
#subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
fig
ax

#
fig, ax = plt.subplots()
ax.barh(y=['CS','EC','ME'], width=[10,20,30])
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
#property of many items at once, it's useful to use the pyplot.setp() function. This will take a list (or many lists) of Matplotlib objects, and attempt to set some style element of each one.

fig, ax = plt.subplots()
ax.barh(y=['CS','EC','ME'], width=[10,20,30])
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[0, 60], xlabel='Total Students', ylabel='Branch',    title='Student Details')


#
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(y=['CS','EC','ME'], width=[10,20,30])
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[0, 60], xlabel='Total Students', ylabel='Branch',    title='Student Details')
