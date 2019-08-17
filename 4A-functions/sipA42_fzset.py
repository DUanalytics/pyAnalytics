# -*- coding: utf-8 -*-
#Frozen Set
#-----------------------------
#%

#The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.
#Due to this, frozen sets can be used as key in Dictionary or as element of another set. But like sets, it is not ordered (the elements can be set at any index)
#frozenset([iterable])

#The frozenset() method optionally takes a single parameter:

#iterable (Optional) - the iterable which contains elements to initialize the frozenset with.
#Iterable can be set, dictionary, tuple, etc.

#The frozenset() method returns an immutable frozenset initialized with elements from the given iterable.

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
type(vowels)
vowels

fSet = frozenset(vowels)
type(fSet)
print('The frozen set is:', fSet)
fSet
print('The empty frozen set is:', frozenset())


#Dictionary : only takes keys
# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
person
type(person)
fSet2 = frozenset(person)
print('The frozen set is:', fSet2)   #only keys


#Like normal sets, frozenset can also perform different operations like union, intersection, etc
#
s = [1,2,3,"hi",1,2,3,5,8,"hi","hello","google"]
s
output = frozenset(s)
print(output)
# Output: frozenset({1, 2, 3, 'google', 5, 8, 'hi', 'hello'})

#Frozenset is an immutable unordered collection of unique elements. It holds collection of element but it does not guarantee the order of the elements in it. As it is immutable we cannot able to update the data once created. when we need to get a unique elements out of group of the repeated elements then we can simply use built-in function "frozenset". we can also use the set but we should only use it when we want to update it afterwards. Because it consumes more memory than frozenset.
#https://learnbatta.com/blog/python-working-with-frozenset-data-type-50/