print(5 + 10)
print(5 - 10)
print(3 * 7)
print(37 / 3)  # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша считают частное от деления нацело
# это как операция div в других языках
print(2 ** 16)  # две звёздочки означают возведение в степень
print(37 % 3)  # процент считает остаток от деления нацело
# это как операция mod в других языках

# a = input() #enter 5
# b = input() #enter 7
# s = a + b
# print(s)

# a = int(input())
# b = int(input())
# s = a + b
# print(s)

##############################

a = 5
b = 7

a, b = b, a

c = -3

a, b, c = c, a, b
a, b, c = 1, 2, 3

a, b, c = input().split(",")

a = 10

a += 1  # a = a + 1
a -= 1  # a = a - 1
a *= 3
a /= 3
a %= 3
a **= 2
a //= 2
