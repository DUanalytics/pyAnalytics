#String Operations
# Sets
S1 = {1,2,3}
type(S1)
S1
S2 = set()
type(S2)
S2.add(4)
S2.add(5)
S2

#Empty Set
S0=set()  # {} creates empty dict, not a set
S0
type(S0)

#Simple Set
S1={'apple','banana',1,2}
S1
type(S1)
#convert to List ???
L1=set(S1)
type(L1)
L1

# Set Comprehensions
import string
s = set(string.ascii_lowercase)
print(s,end=' ')

from string import ascii_uppercase, ascii_lowercase
sl=set(ascii_lowercase)
sL=list(ascii_lowercase)

su=list(ascii_uppercase)
print(sl,su, sep='-', end=' ')
sl.sort()  # error
sL.sort()
sL
#cannot sort sets


alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))
print(alphabet, end='')

ALPHABET = []
for letter in range(65, 91):
    ALPHABET.append(chr(letter))
print(ALPHABET, end='')

# Use map to create lowercase alphabet
alphabet1 = map(chr, range(97, 123))
print(list(alphabet1))

for ch in map(chr, range(97, 123)):
    print(ch, end='')

L2= [chr(x) for x in [66,53,0,94]]
L2
L2= [chr(x) for x in range(97,123)]
print(L2, end=' ')

[*map(chr, [66, 53, 0, 94])]
[*map(chr, range(97,123))]
