#Topic: Bunch Type _ Not Complete
#-----------------------------
#libraries
#Container object for datasets
#Dictionary-like object that exposes its keys as attributes.
b = Bunch()
b.hello = 'world'
b = Bunch(a=1, b=2)
type(b)
b['b']
b.b

#Links
#https://github.com/dsc/bunch
b.a = 3
b['a']
b.c = 6
b['c']

