#Topic: Frozen Sets
#-----------------------------
#The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable. 
#syntax : frozenset([iterable])
#Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.
#Due to this, frozen sets can be used as key in Dictionary or as element of another set. But like sets, it is not ordered (the elements can be set at any index)

#Sets are mutable, and may therefore not be used, for example, as keys in dictionaries.
#Another problem is that sets themselves may only contain immutable (hashable) values, and thus may not contain other sets.
#Because sets of sets often occur in practice, there is the frozenset type, which represents immutable (and, therefore, hashable) sets

fzs1 = frozenset([1, 2, 3])
fzs1
type(fzs1)

fzs2 = frozenset([2, 3, 4])

fzs1.union(fzs2) #all numbers
fzs1.intersection(fzs2)  #common


#Sets may only contain immutable (hashable) values, and thus may not contain other sets, in which case frozensets can be useful. Consider the following example:
a = set([1, 2, 3])
b = set([2, 3, 4])
a.add(b)
a.add(frozenset(b))
a
#--
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The frozen set is:', fSet)

#used in dictionary # random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet)
#Like normal sets, frozenset can also perform different operations like union, intersection, etc.
#links
#https://www.python-course.eu/python3_sets_frozensets.php
