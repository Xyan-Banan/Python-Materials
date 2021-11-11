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
print(f"{c2.teacher} {c2.students}")

print("Calling clear method")
c2.students.clear()
print(f"{c.teacher} {c.students}")
print(f"{c2.teacher} {c2.students}")


print("##############################################")


class Class2:
    def __init__(self, teacher=""):
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

# Part 2


class Class3:
    def __init__(self, teacher=None):
        self._teacher = teacher  # treated as non-public
        self.__students = []  # name mangling to _Class3__student

    def addStudent(self, student):
        if type(student) is str:
            self.__students.append(student)
        else:
            raise ValueError("Illegal argument type")

    def __str__(self):
        return f"{self._teacher} {self.__students}"


complitlyClosedClass = Class3("Socratus")
complitlyClosedClass.addStudent("Plato")
complitlyClosedClass.addStudent("Aristotle")
try:
    complitlyClosedClass.addStudent(1)
except ValueError as e:
    print(e)

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


s = Student("Frodo", "Baggins")
print(f"inherited with no changes: {s}")


class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self._grade = grade
        self.__secretProp = "Cool physicist"

    def __str__(self):
        # return f"{self._firstname} {self.__lastname} {self._grade}" # лучше, но не можем использовать из-за области видимости __lastname
        return super().__str__() + f" {self._grade}"

    # def __repr__(self) -> str:
    #     return super().__repr__()


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

print(s)
s2 = Student("Issac", "Newton", 3.0)
studs = [s, s2]
print(studs)
for stud in studs:
    print(stud, end=" | ")
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

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


m = Mapping([1, 2, 3, 4])
print(m.items_list)
m.update("a b c".split())
print(m.items_list)
m2 = MappingSubclass([5, 4, 3, 2, 1])
print(m2.items_list)
m2.update("a b c".split(), (1, 2, 3))
print(m2.items_list)

# MappingSubclass._Mapping__update = MappingSubclass.update
m3 = MappingSubclass([1, 2, 3])

del m.items_list
# del m.update
# print(m.items_list)
# print(m2.items_list)

###########################################################


def helloFunc():
    print("hello")


def helloFuncSelf(self):
    print(f"field = {self.field}")


class A:
    def __init__(self, function=None) -> None:
        self.func = helloFunc
        self.funcSelf = function
        self.field = 10


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


# Полиморфизм на уровне классов
b = B(helloFuncSelf)
c = C()
d = D()

# у всех объектов будет поле 'field' и поле 'func', т.к. они - наследники одного класса
lst = [b, c, d]
for i in lst:
    i.field
    i.func()


# разница между добавленными извне методами
# метод func не принимает параметров, поэтому не может получить информацию из объекта
b.func()
# метод funcSelf принимает один параметр,
# поэтому можно получить информацию из объекта, но нужно для этого передать объект как аргумент
b.funcSelf(b)
b.field

# можно удалить поля или ссылки на функции из объектов. на другие объекты это не повлияет
del b.func
del b.funcSelf
# b.func()
# b.funcSelf()

# Полиморфизм на уровне методов (его нет)
# каждое новое описание - удаляет старое
def a(i):
    return i * i


print(a(i=5))


def a(k, j):
    return k * j


print(a(5, 7))

# в такой форме метод позволяет передать неизвестное количество аргументов
# полимерфизм по количеству аргументов
def a(*args):
    if len(args) == 1:
        pass
    elif len(args) == 2:
        pass


a(1, 2, 3, 4, 5)


def a(param):
    if type(param) is str:
        print("this code works only with STRINGS")
    elif type(param) is int:
        print("this code works only with INTEGERS")


a("text")
a(10)
