#Statistics - t-test - Independed samples
#samples from different population

from scipy.stats import ttest_ind

data1 = [3,4,2,4,2]
data2 = [3,6,3,2,3]
data1, data2

stat, p = ttest_ind( data1, data2)
stat, p
print('stat=%.3f, p=%.3f' % (stat, p))

p

if p > .05 : print(p, 'Sample could be from same distribution')
else: print(p, 'Sample from different population : p value is significant; Means do not match')

ttest_ind(data1, data2)  #theoritical distribution
