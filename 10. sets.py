numbers = {6, 7, 1, 2, 3, 4, 4, 4, 5, 6, 1, 3, 5}
print(numbers)

s = set("hello")
print(s)

s |= {1}  # equal to s = s | {1} or s.update({1})
s &= set(
    "wierd world"
)  # equal to s = s & set("wierd world") or s.intersection_update(set("wierd world"))
s -= set("hell")  # equal to s = s - set("hell") or s.difference_update(set("hell"))
print(s)

a = set(range(3))
b = set(range(10))
print(a, b)
print(a <= b)
print(a < b)

a = set(range(10))
print(a, b)
print(a <= b)
print(a < b)
