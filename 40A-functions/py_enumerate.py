#Enumerate
#-----------------------------
#%

# for loop
top3 = ['bob', 'alice', 'ted']
range(len(top3))

for n in range(len(top3)):  print(n, top3[n])
for n in range(len(top3)):  print(n + 1, top3[n])
 
#enumerate()
#Another option is to use Python’s enumerate() which will take an iterable and give you back an iterable of index, value pairs.

enumerate(top3)
# use list() to turn it into a list which allows us to view its contents.
list(enumerate(top3))
# we can see each item produced by enumerate() is a tuple with 2 elements: the index and the name.

for n, name in enumerate(top3):   print(n + 1, name)
#use n + 1 because the indexing starts at 0 however could have also used the start argument of enumerate() to specify what number to start counting from
for n, name in enumerate(top3, start=1):  print(n, name)

#we’re supplying 2 variable names here to the for loop n and name. What’s happening here is called sequence unpacking

n, name = 1, 'Bob'
n
name
#Python unpacks the right hand side and stores it into the corresponding variables on the left hand side.

#The same thing happens with n, name in our for loop - each tuple produced by enumerate() gets unpacked.

#more
#https://kaijento.github.io/2017/04/28/python-for-loops/