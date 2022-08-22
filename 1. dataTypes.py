# NUMBERS
########
a = 5
print(a, "is of type", type(a))  # int = integer

a = 2.0
print(a, "is of type", type(a))  # float = floating point

a = 1 + 2j
print(a, "is of type", type(a))
print(a, "is complex number?", isinstance(1 + 2j, complex))

float(5)  # 5.0

# STRINGS
########
print('В тексте есть "двойные" кавычки')
print("В тексте есть 'одинарные' кавычки")
s = "This 'sunny' is a string"
print(s)
s = """A multiline
string"""
print(s)
s = "Hello world!"
print("s[4] = ", s[4])  # s[4] = 'o'
print("s[6:11] = ", s[6:11])  # s[6:11] = 'world'
# s[5] ='d' # Generates error. Strings are immutable in Python

name = "Джон"
surname = "Смит"
fio = name + " " + surname
print(fio)

name = "Pavel"
# name[0] = 'p'

# TYPE CASTING
#############
# Conversion from float to int will truncate the value (make it closer to zero).
int(10.6)  # 10
int(-10.6)  # -10
int(False)  # 0
int("10")  # 10
# int("10.5") #error
print(int(float("10.5")))

print(5 + 5 == 11)
print(5 + 5 == 10)

float(True)  # 1.0
float(False)  # 0.0
float("10")  # 10.0
float("10.5")  # 10.5

# Conversion to and from string must contain compatible values.
float("2.5")  # 2.5
str(25)  #'25'
# int('1p') #error

bool(0)  # False
bool(1)  # True
bool(-1)  # True
bool(10)  # True
bool(0.13332)  # True
bool(-1.5)  # True
bool(0.0)  # False
bool(10 + 6j)  # True
bool(0 + 15j)  # True
bool(0 + 0j)  # False
bool("Apple")  # True
bool("z")  # True
bool("")  # False

str(10)  #'10'
str(3.14)  #'3.14'
str(True)  #'True'
str(False)  #'False'
str(10 + 5j)  #'10+5j'
