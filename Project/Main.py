import os
import random
import time
import Actions

os.system("clear")
loading = True
loadingtext=["Booting Up","Opening","Starting Up","Loading",""]
while loading:
    print(loadingtext[random.randint(0, 3)])
    time.sleep(random.randint(1, 5)/10)
    if random.randint(1, 5) == 5:
        loading = False
print("Finished")

time.sleep(1)
def drawrandmap(xmin,xmax,ymin,ymax):
    b = []
    lenx = random.randint(xmin, xmax)
    leny = random.randint(ymin, ymax)
    print(lenx)
    print(leny)
    rmap = []
    for i in range(leny):
        b = []
        for j in range(lenx):
        
            d=random.randint(1, 4)
            if d==1:
                b.append("0")
                print("~", sep="",end="")
            else:
                b.append("1")
                print(" ", sep="",end="")
        rmap.append(b)
        print(" ")
'''xmin=int(input())
xmax=int(input())
ymin=int(input())
ymax=int(input())'''
#for i in range(10):
    #drawrandmap(xmin,xmax,ymin,ymax)
#Action.mapMake(100,40)

Actions.Walk(0,0)
