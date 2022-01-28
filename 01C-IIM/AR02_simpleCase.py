#python : DUP - Topic : Association Rules.......
#https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6
#https://efficient-apriori.readthedocs.io/en/latest/
#simplest example on AR

from efficient_apriori import apriori
teams = [('Paridhi', 'Abir', 'Varun'), ('Paridhi', 'Sai', 'Varun', 'Dhiraj'), ('Varun', 'Bharath', 'Sai','Aditya'),('Sai','Bharath')]
teams
help(apriori)#help on algo
itemsets, rules = apriori(transactions =  teams, min_confidence=.6, min_support=.5)
rules
print(rules)

itemsets, rules = apriori(teams, min_support=0.25,  min_confidence=.6)
# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) >= 1, rules)
teams
# Prints the rule and its confidence, support, lift, ...
for rule in sorted(rules_rhs, key=lambda rule: rule.lift): print(rule) 
itemsets[0] #blank transaction
itemsets[1] #single item, how many times
itemsets[2]  #two items, how many times
itemsets[3]
itemsets[4]
itemsets
rules


#from different library
from apyori import apriori
association_rules = apriori(teams, min_support=0.5, min_confidence=0.6, min_lift=1, min_length=2)
association_results = list(association_rules)
print(association_results)
print(association_results[1])
print(len(association_results))


#mlextend
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
frequent_itemsets = apriori(teams, min_support= support_threshold, use_colnames = True)
teams
#convert transactions to df
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(teams)
te_ary
te.columns_
dfTeams = pd.DataFrame(te_ary, columns=te.columns_)
dfTeams
teams
#which student in which team - T/ F
support_threshold =.30
frequent_itemsets = apriori(dfTeams, min_support= support_threshold, use_colnames = True)
frequent_itemsets
teams
print(frequent_itemsets) 

frequent_itemsets = apriori(dfTeams, min_support= .3, use_colnames = True)
frequent_itemsets
print(frequent_itemsets) #dataframe with the itemsets

#arules - build from frequent itemsets
supportRules = association_rules(frequent_itemsets, metric="support", min_threshold = .2) 
print(supportRules)
supportRules.head()
print(supportRules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

confidenceRules = association_rules(frequent_itemsets, metric="confidence", min_threshold = .8) 
print(confidenceRules)
confidenceRules.head()
print(confidenceRules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
confidenceRules[(confidenceRules.support > .3) & (confidenceRules.lift > 2)]

frequent_itemsets[ frequent_itemsets['itemsets'] == {'Paridhi'} ]
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)

frequent_itemsets[ (frequent_itemsets['length'] >= 3) & (frequent_itemsets[ 'support'] >= 0.3) ]
