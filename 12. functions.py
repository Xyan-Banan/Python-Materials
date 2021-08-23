def my_function():
    print("Hello from a function")

# print(my_function())

def greet(name):
    return f"Hello, {name}!"

print(greet("Michael"))

def greet(fname, lname):
    print(f"Hello, {fname} {lname}!" )

greet("Michael","Sokolov")
greet(lname="Wayne (with keywords)",fname="Bruce")
greet("Clark",lname="Kent")
# greet("Parker",fname="Peter") #causes multiple values for argument 'fname'
# greet(fname="Harry","Potter") #causes positional error

# task 1: написать функцию, которая возвращает максимальное из двух чисел
def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(3, 5))
print(max(5, 3))

def greet(fname="Ivan", lname="Ivanov", patr="Ivanovich"):
    print(f"Hello, {lname} {fname} {patr}! \t(with default values)")

greet()
greet("Petr")
greet("Petr", "Petrov", "Petrovich")
greet(lname="Zhukov")

print(1,2,3,5,6,7)

def greetGrour(name,*names):
    print(f"Hello, {name}! \t(required parameter)" )
    for n in names:
        print(f"Hello, {n}! \t(from *names)" )

# greetGrour()
greetGrour("Adam")
greetGrour("Bob", "Curt", "Daniel", "Eric") #arbitary arguments
# greetGrour("Frank", name="George", "Henry") #causes positional error
# greetGrour("Frank", "George", name="Henry") #causes multiple values for argument 'name'
# greetGrour( names=[ "Frank", "George"], name="Henry")

def greetGrour2(*names, name):
    print(f"Hello, {name}! \t(required parameter)" )
    for n in names:
        print(f"Hello, {n}! \t(from *names)" )

# greetGrour2("Ivan")
greetGrour2(1,2,3,4,5,name="Ivan")

#######################################################################################

print("### Passing **kwargs into function ###")

def greetPerson(**person):
    print("Hello, {name} {}! \t(from **person)".format(person["lname"],name=person["fname"]))

greetPerson(fname="Joe", lname="Jhonas")
# greetPerson(fname="Joe") #causes KeyError in function because missing keyword "lname"

print("### Passing list into function ###")

def greetGrour3(groupList):
    for person in groupList:
        print("Hello, {} {}! \t(person from groupList)".format(person.get("fname","Noname"), person.get("lname","")) )

group = []
group.append({"fname":"Kurt","lname":"Konnors"})
group.append(dict([("fname","Linus"),("lname","Torvalds")]))
group.append(dict(fname="Marty",lname="McFly"))
group.append(dict(fname="Nicolas"))
group.append(dict(lname="Otto"))
group.append(dict())
print(group)
greetGrour3(group)

print("### Unwrapping list value as **kwargs function ###")

greetPerson(**group[0])

print("### Recursion ###")

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n-1)

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res


for i in range(6):
    print(factorial(i), fact(i))

# n = 10**2
# print(fact(n),factorial(n))

# 1 1 2 3 5 8 13 21

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib2(n):
    if n == 1 or n == 2:
        return 1
    n1 = 1
    n2 = 1
    for i in range(n-2):
        res = n1 + n2
        n2 = n1
        n1 = res
    return res

for i in range(1,11):
    print(fib(i), end=" ")
print()

for i in range(1,11):
    print(fib2(i), end=" ")
print()

print("### Pass statement ###")

def emptyFunc():
    pass #TODO - complete this function

if 1 + 1 == 2:
    print("math is ok")
    pass
    print("but this is to be expected")

for i in range(10):
    pass

class Person:
    pass #TODO - complete this class

print("### Global and Local variables ###")

def f():
    print(a)

a = "My cool global variable"
f()

print('--------')

def f2():
    b = "My cool LOCAL variable"

f2()
# print(b)

print('--------')

def f3():
    global c
    f = 123
    c = "New cool value"
    print(c)

c = "Cool Global C"
f3()
print(c)