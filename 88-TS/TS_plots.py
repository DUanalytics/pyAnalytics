#Topic: Visualisation 
#-----------------------------
#libraries
https://towardsdatascience.com/data-visualization-using-matplotlib-16f1aae5ce70


fig = plt.figure(figsize=(10,6))
ax1 = fig.add_axes([0,0,1,2])
ax1 = fig.add_axes([0.05,0.65,.5,.3])
ax1.set_title("A vs B")

ax1.plot(data['Date'], data['A'], color='green')
ax2.plot(data['Date'], data['B'], color='blue')
plt.show();

#various Stocks
fig=plt.figure(figsize=(15,7))
fig.suptitle('Stock Prices - Multiple Stocks', fontsize=20)

ax1=fig.add_subplot(231)
ax1=plot(data['Date'], data['A'], color='green')
ax1.set_title('A Stock')

---
ax1=fig.add_subplot(236)
ax1=plot(data['Date'], data['F'], color='green')
ax1.set_title('F Stock')
fig.show();

