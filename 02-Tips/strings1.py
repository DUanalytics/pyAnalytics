#
#-----------------------------
#%

s = "ZWzaAd"
print(''.join(sorted(s)))


#Strings
#Eg1
a = 'molecular simulation'
print(a)
a = "molecular simulation"
print(a)
#Eg2
a = "Scott's Class"
print(len(a))
print(a)
#Eg3
a = "hello" * 3
print(a)

#Eg4
s = """ This is a triple-quoted string
	It will pick up the line break in this multi line sentence."""
print(s)

#Eg5
print(" this string has \n line break")
print(" Here is \t tab")
print(" Scott \'s student said, \" I like this course \" ")
print(" Use backlash character \\ ")
print(r" this will not recognise \t and \n" )

#Eg6
str(1)
str(1.0)
str(1+2)

s = "Value of pi is %8.3f" % 3.141591
print(s)
