a = [1, 2.5, '3', "hello", ["this","is","inner","list"]]

print(f"list: {a}")
print(f"list length: {len(a)}")
print(a[0])
a[0] = -100500
print(a[-1])
print(a[4][2], a[-1][2], a[-1][-2])

for i in a:
    print(i, end =' ')
print()

for i in range(len(a)):
    print(i, a[i])
print()

print(a[:2],a[2:])
print(a[-1::-1])

print(f"even elements: {a[::2]}")
print(f"reverse list: {a[::-1]}")

print(a[::2],a[1::2])

a = list(range(10))
for i in a:
    print(i, end =' ')
print()

string = "Hello world!"
print(f"string: {string} length {len(string)}")
for i in string:
    print(i, end=' ')
print()

print(f"even string elements: {string[::2]}")
print(f"reverse string: {string[::-1]}")