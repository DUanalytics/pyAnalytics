#Topic: AR - efficient apriori
#-----------------------------
#libraries

#pip install efficient_apriori
from efficient_apriori import apriori
transactions = [('eggs', 'bacon', 'soup'),    ('eggs', 'bacon', 'apple'), ('soup', 'bacon', 'banana')]  #avoids duplicates
transactions
itemsets, rules = apriori(transactions, min_support=0.5,  min_confidence=1)
print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]

rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.lift): print(rule)
# Prints the rule and its confidence, support, lift, ...



 