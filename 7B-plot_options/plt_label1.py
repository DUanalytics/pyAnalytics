#Advances - Labelling
#-----------------------------
#%
import matplotlib as mpl
workshop1
fig, ax = plt.subplots(figsize=(12, 4))
workshop1.attendance.plot()
#---------
fig, ax = plt.subplots(figsize=(12, 4))
workshop1.attendance.plot(ax=ax)
ax.text('2019-7-15', 30, "One month before Indepedence Day")


#
# Add labels to the plot
style = dict(size=10, color='gray')
fig, ax = plt.subplots(figsize=(8, 4))
workshop1.attendance.plot(ax=ax)
ax.text('2019-7-16', 35, "Independence Day", ha='center', **style)

#Label Axis
ax.set(title='Attendance during the Workshop', ylabel='Daily Attendance')
# Format the x axis with centered month labels
#ax.xaxis.set_major_locator(mpl.dates.DateLocator())
#ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%d'))

#-------
#ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
#ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=7))
#ax.xaxis.set_major_formatter(plt.NullFormatter())
#ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%d'));


#%%%
#Annotations wrt Data, Axes and Figures
fig, ax = plt.subplots(facecolor='lightgray')
ax.axis([0, 10, 0, 10])
# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure);
#run upto here first and next 5 lines also
# if we change the axes limits, it is only the transData coordinates that will be affected, while the others remain stationary:
ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)
fig     