import random as rd
import time 
import re
def looper(n, item):
    i = 0
    #$ii = 0
    lil = []
    #while ii < 10:
    for x in range(20):
        while i < int(n):
            i += 1
            lil.append("%s" % str(item)) 

            string = "".join(str(b) for b in lil)
            return string

#x = y = input("eveb amounts, then how many?")

# make this so the number of items in the array keeps increasing
v = 10 
looper = looper(12, "gay")
while True:
    #time.sleep(3)    
    #v += 1
    print(looper)
    if str(looper) == "":
        break
    else:
        continue