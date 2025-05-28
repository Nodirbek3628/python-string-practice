import random

name = input("Ismingizni kiriting:")
familya = input("Familiyangizni kiriting:")

index = name[0]
index01 = familya[0]

c = f"{name}.{familya}"
d = f"{familya}_{name}"
v = f"{index}{familya}.{random.randint(1,100)}"
s = f"{familya}{index01}"



print(c)
print(d)
print(v)
print(s)