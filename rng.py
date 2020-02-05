import os, random

lil = []
i = 0
n = int(input("how much?"))/2
while i < n:
    i += 1
    lil.append(random.randint(10,100))

#print(int(n))
#for x in lil:
#while True:
joined = "".join(str(x) for x in lil[:int(n)*2])
print("+91" + joined)

