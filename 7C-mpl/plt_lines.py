#Vertical and Horizontal Lines
#-----------------------------
#%

Common axis
for ax in axes:
    ax.set_xlabel('Common x-label')
    ax.set_ylabel('Common y-label')
#number

xposition = [0.3, 0.4, 0.45]
for xc in xposition:
    plt.axvline(x=xc, color='k', linestyle='--')

#Time Series
    
    
    fig.add_subplot(111, frameon=False)
    
    
    fig = plt.figure()
ax = fig.add_subplot(111)    # The big subplot
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

ax1.loglog(x, y1)
ax2.loglog(x, y2)

# Set common labels
ax.set_xlabel('common xlabel')
ax.set_ylabel('common ylabel')

ax1.set_title('ax1 title')
ax2.set_title('ax2 title')

plt.savefig('common_labels.png', dpi=300)
