class Box:
    value = 0

b = Box()
print(f"b.value = {b.value}")
b.value = 10
print(f"b.value after change = {b.value}")

bb = Box()
print(f"bb.value = {bb.value}")
bb.value = "Hello world"
print(f"bb.value after change = {bb.value}")
print(f"b.value = {b.value}")

print("##############################################")

box = Box()
box.aaa = 5
print(box, box.aaa)

def f():
    print("Hello, i'm a box")

box.coolFunction = f
box.coolFunction()

print("##############################################")

class Class:
    teacher = ""
    students = []

c = Class()
c.teacher = "Mrs. Smith"
c.students.append("John")
print(f"{c.teacher} {c.students}")

c2 = Class()
c2.teacher = "Splinter"
c2.students.append("Donatello")
print(f"{c.teacher} {c.students}")

print("Calling clear method")
c2.students.clear()
print(f"{c.teacher} {c.students}")
print(f"{c2.teacher} {c2.students}")

print("##############################################")

class Class2:
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []

c3 = Class2("Rick")
c3.students.append("Morty")
print(f"{c3.teacher} {c3.students}")
c4 = Class2("Batman")
c4.students.append("Robin")
print(f"{c4.teacher} {c4.students}")

print("Copying list from c3 to c4")
c4.students = c3.students
c4.students.append("blablabla")
print(f"c4: {c4.teacher} {c4.students}")
print(f"c3: {c3.teacher} {c3.students}")

print("Clearing c4's list")
c4.students.clear()
print(f"c4: {c4.teacher} {c4.students}")
print(f"c3: {c3.teacher} {c3.students}")

print("##############################################")

#Part 2

class Class3:
    def __init__(self, teacher = None):
        self._teacher = teacher #treated as non-public
        self.__students = []    #name mangling to _Class3__student

    def addStudent(self,student):
        if(type(student) is str):
            self.__students.append(student)
        if(type(student)  is int):
            print("Illegal argument type")
            # raise AttributeError("")

    def __str__(self):
        return f"{self._teacher} {self.__students}"


complitlyClosedClass = Class3("Socratus")
complitlyClosedClass.addStudent("Plato")
complitlyClosedClass.addStudent("Aristotle")
complitlyClosedClass.addStudent(1)

print(complitlyClosedClass._teacher)
# print(complitlyClosedClass.__students)
print(complitlyClosedClass._Class3__students)
print(complitlyClosedClass)

print("##############################################")

class Person:
    def __init__(self, fname, lname):
        self._firstname = fname
        self.__lastname = lname

    def __str__(self):
        return f"{self._firstname} {self.__lastname}"

p = Person("Peter", "Parker")
print(p)

class Student(Person):
    pass

s = Student("Frodo","Baggins")
print(f"inherited with no changes: {s}")

class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self._grade = grade
        self.__secretProp = "Cool physicist"

    def __str__(self):
        # return f"{self._firstname} {self.__lastname} {self._grade}"
        return super().__str__() + f" {self._grade}"

s = Student("Albert", "Einstein", 5.0)

print(f"inherited with additional property and overwritten __str__ method: {s}")
str(s)

print("##############################################")

print(f"name = {s._firstname}")

try:
    print(f"lastname = {s._Student__lastname}")
except AttributeError as e:
    print(e)

print(f"lastname = {s._Person__lastname}")
print(f"grade = {s._grade}")
print(f"secret property = {s._Student__secretProp}")

print("##############################################")

s2 = Student("Issac","Newton",3.0)
studs = [s,s2]
print(studs)
for stud in studs:
    print(stud, end = " | ")
print()

def r(self):
    return f"Student('{self._firstname}','{self._Person__lastname}',{self._grade})"

Student.__repr__ = r

print(studs)
studs.append("Socratus")
studs.append(1)
studs.append(None)
print(studs)

print("##############################################")

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

m = Mapping([1,2,3,4])
print(m.items_list)
m.update("a b c".split())
print(m.items_list)
m2 = MappingSubclass([5,4,3,2,1])
print(m2.items_list)
m2.update("a b c".split(),(1,2,3))
print(m2.items_list)

# MappingSubclass._Mapping__update = MappingSubclass.update
m3 = MappingSubclass([1,2,3])

del m.items_list
# del m.update
# print(m.items_list)
# print(m2.items_list)

###########################################################

def a(i):
    return i*i

def a(k,j):
    return k*j

print(i = a(5))
print(a(5,7))