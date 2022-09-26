x = 5
y = 7

x > y  # False
x < y  # True
x == y  # False
x != y  # True

x >= y  # False
x <= y  # True

not (x > y) == x <= y
not (x < y) == x >= y
not (x == y) == x != y
not (x != y) == x == y

not (x >= y) == x < y
not (x <= y) == x > y

fruit1 = "Apple"

print(fruit1 == "Apple")  # True
print(fruit1 != "Apple")  # False
print(fruit1 < "Apple")  # False
print(fruit1 > "Apple")  # False
print(fruit1 <= "Apple")  # True
print(fruit1 >= "Apple")  # True

fruit1 == "apple"  # False
fruit1 != "apple"  # True
fruit1 > "apple"  # False    Код символа 'А' имеет меньшее значение чем 'а'
fruit1 < "apple"  # True

fruit1.lower() == "apple"  # True
fruit1.upper() == "APPLE"

isRaining = False
not (isRaining)  # False
isGameOver = False
not (isGameOver)  # True

isGoinRaining = False

isRaining or isGoinRaining and False  # True
isRaining and isGoinRaining  # False

# not
# and
# or

a = 10
b = 5
1 < a < 100
(1 < a) and (a < 100)
print(1 < a < 100)
print(1 < b < a < 100)
print(1 < a < b < 100)
5 <= a < b == 10 < 100

15 < a < 23
a in range(15, 24)

n = int(input())

if n % 2 == 0:
    res = "even"
else:
    res = "odd"

print(res)

print("even" if int(input()) % 2 == 0 else "odd")
