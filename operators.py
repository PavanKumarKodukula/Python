print("Arithmetic Operators")

a = 100
b = 25

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division", a // b)
print("Modulus", a % b)
print("Exponentiation:", a ** b)
print()

print("Assignment Operators")

a = 100

a += 3
print(a)
a -= 3
print(a)
a *= 4
print(a)
a /= 3
print(a)
a //= 3
print(a)
a %= 4
print(a)
a **= 2
print(a)
print()

print("Relational (Comparison) Operators")

a = 200
b = 290

print("Less than:", a < b)
print("Greater than:", a > b)
print("Less than or equal:", a <= b)
print("Greater than or equal:", a >= b)
print("Equal to:", a == b)
print("Not equal to:", a != b)
print()

print("Logical Operators")

a = 250
b = 350
c = 209
d = 890

print("and:", a < b and d >= c)
print("or:", a >= b or b // 20 > 0)
print("not:", not (a == b))
print()

print("Bitwise Operators")

a = 115
b = 625
c = 393
d = 294

print("Bitwise AND:", a & b)
print("Bitwise OR:", c | d)
print("Bitwise XOR:", a ^ d)
print("Bitwise NOT:", ~a)
print("Left Shift:", c << 4)
print("Right Shift:", d >> 1)
print()

print("Membership Operators")

numbers = [120, 125, 130]

print("120 in numbers:", 120 in numbers)
print("140 in numbers:", 140 in numbers)
print("140 not in numbers:", 140 not in numbers)
print()

print("Identity Operators")

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)
print("list1 is not list3:", list1 is not list3)
print()