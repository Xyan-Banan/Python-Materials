if True:
    print("True!!!")
else:
    print("False(((")

if False:
    print("True!!!")
else:
    print("False(((")

condition = True

if condition:
    print("True!!!")
else:
    print("False(((")

x = 5
if x > 3:
    print("True!!!")
else:
    print("False(((")

condition = x > 3
if condition:
    print("True!!!")
else:
    print("False(((")


x = 5
condition = x > 3 or not(x > 1)
if condition:
    print("True!!!")
else:
    print("False(((")

x = 0
if x > 0:
    print("x > 0")
elif x < 0:
    print("x < 0")
else:
    print("x = 0")

a = 0

+a
-a

a = 10
a + 10
a - 10

text = ""
if(a > 0):
    text = "positive"
else:
    text = "negative"

text = "positive" if (a > 0) else "negative"
a = -a if(a > 0) else a
print(a)
print(-a if(a > 0) else a)

a = 1
b = 2
c = 3

if(a < c):
    if(a < b):
        print(a)
    else:
        print(b)
else:
    if(c < b):
        print(c)
    else:
        print(b)
