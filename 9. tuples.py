a = ()
a = (1,2,3)
a = 1,2,3

b,c,d = a
print(b,c,d)

e = b,c,d
print(e)

#b,c = e #Value error
#print(b,c) 

a = ("hello") #just variable
a = ("hello",) #one element tuple
a = tuple("hello")

for i in a:
    print(i, end = ' ')

print()
print("".join(a))