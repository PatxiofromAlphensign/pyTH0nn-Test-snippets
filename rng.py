import os, random

lil = []
i = 0
while i < 10:
    i += 1
    lil.append(random.randint(0,100))

number = "".join(str(x) for x in lil)
print(number)