#Statistics - Chi Squared

from scipy.stats import chi2_contingency
table =[[10,20,30], [6,9,17]]
table
stat, p, dof, expected = chi2_contingency(table)
stat
p
print('stat=%.3f, p=%.3f' % (stat, p))

if p > .05 : print(p, 'Could be Independent')
else: print(p, 'Could be dependent : p value is significant')
