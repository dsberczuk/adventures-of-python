import os
import random
import time
import sys
from Item import Item
from Effects import Effect
from Targets import Characters
from termcolor import colored,cprint

def Walk(x,y):
    ysize=20
    xsize=50
    newx=y
    newy=x
    map=[]
    mountainList =[]
    townList=[]
    mountainhere = False
    ttownhere=False
    qtownhere=False
    treasurehere=False
    inBoat = False
    qtowns = []
    ttowns = []
    treasure=[[3,3]]
    gold=0
    colorvariation = False
    rand = 0
    player = Characters(20,0,10,10,10,[])
    moText = ["This a a mountain","This is a tall mountain","There is a coin on the ground"]
    GiveCoin=Effect(player,player.gold,100)
    CoinBag=Item("Coin Bag",10,"x",5)
    ItemsDict=dict([("coin bag",CoinBag)])
    for m in range(ysize):
        temp=[]
        b=0
        for a in range(xsize):
            if b ==0:
                if random.randint(1,4) <=3:                         #Water/Land Frequency
                    p=0
                    s=" "
                else:
                    p=1
                    s="O"
            else:
                if random.randint(1,8) ==4:                         #Water/Land Frequency for Tiles Adjcaent to Land
                    p=0
                    s=" "
                else:
                    p=1
                    s="O"
            print(s,sep="",end="")
            temp.append(p)
            b=p
        map.append(temp)
        print("")
    for g in range(random.randint(50,100)):                         #Make Towns
        tEditX = random.randint(1,48)
        tEditY= random.randint(1,18)
        if map[tEditY][tEditX] == 1:
            townList.append([tEditY,tEditX])
    for p in range(len(townList)):                                  #New Towns
        if random.randint(0,5) == 0:
            qtowns.append(townList[p])
        else:
            ttowns.append(townList[p])
    for p in range(random.randint(10,50)):                          #Make Mountains
        tEditX = random.randint(1,48)
        tEditY= random.randint(1,18)
        if map[tEditY][tEditX] == 1:
            mountainList.append([tEditY,tEditX])
        if random.randint(2,3)==3:
            for i in range(3,5):
                mrx =random.randint(-1,1)
                mry=random.randint(-1,1)
                if map[tEditY-mry][tEditX-mrx] <-1:
                    mountainList.append([tEditY-mry,tEditX-mrx])
                    if random.randint(2,3)==3:
                      for i in range(3,5):
                        mrx =random.randint(-1,1)
                        mry=random.randint(-1,1)
                        if map[tEditY-mry][tEditX-mrx] < -1:
                            mountainList.append([tEditY-mry,tEditX-mrx])
    while True:
        
        
        dir=input()
        if dir == "North" or dir == "north" or dir == "w" and map[y-1][x] == 1:
            newy = y-1
        if dir == "South" or dir == "south" or dir == "s" and map[y+1][x] == 1:
            newy = y+1
        if dir == "West" or dir == "west" or dir == "a" and map[y][x-1] == 1:
            newx = x-1
        if dir == "East" or dir == "east" or dir == "d" and map[y][x+1] == 1:
            newx = x+1
        if dir == "b":
            for g in range(len(map)):
                for p in range(len(map[1])):
                    if map[g][p] ==0:
                        map[g][p] =1
                    elif map[g][p] ==1:
                        map[g][p] =0
            if inBoat == True:
                inBoat = False
            else:
                inBoat = True
        if dir == "u":
            item=input()
            if item in ItemsDict:
                print("*")
                if ItemsDict[item].quantity>0:
                    ef=ItemsDict[item]
                    ItemsDict[item].quantity-=1
                    print(ItemsDict[item].quantity)
            else:
                print("--")
            time.sleep(1)
        else:
            print("Unable to move there")
        map[y][x]=1
        x=newx
        y=newy
        map[y][x]=2
        qtowns=townList
        #Update map
        os.system("clear")
        if colorvariation == True:
            colorvariation=False
        else:
            colorvariation=True
        for a in range(ysize):
            for b in range(xsize):
                for mo in range(len(mountainList)):
                    if mountainList[mo][0] == a and mountainList[mo][1]==b:
                        mountainhere=True
                for tr in range(len(treasure)):
                    if treasure[tr][0]==a and treasure[tr][1]==b:
                        treasurehere=True
                for to in range(len(ttowns)):
                    if ttowns[to][0] == a and ttowns[to][1]==b:
                        ttownhere=True
                for to in range(len(qtowns)):
                    if qtowns[to][0] == a and qtowns[to][1]==b:
                        qtownhere=True
                if mountainhere == True:
                    cprint("A","grey",sep='',end="")
                    mountainhere=False

                elif ttownhere == True:
                    print("T",sep='',end="") 
                    ttownhere=False
                elif qtownhere == True:
                    print("Q",sep='',end="")
                    qtownhere=False
                elif treasurehere == True:
                    cprint("X","magenta",sep='',end="")
                    treasurehere=False
                elif map[a][b] == 2:
                    cprint("","red",attrs=['bold'],sep='',end="")
                elif map[a][b] == 1:
                    
                    if inBoat == True:
                        
                        if colorvariation == True:
                            cprint("~","blue",sep='',end="")
                            colorvariation=False
                        else:
                            cprint("~","cyan",sep='',end="")
                            colorvariation=True
                    else:
                        cprint("0","green",sep='',end="")
                elif map[a][b] == 0:
                    if inBoat == True:
                        cprint("0","green",sep='',end="")
                    else:
                        if colorvariation == True:
                            cprint("~","blue",sep='',end="")
                            colorvariation=False
                        else:
                            cprint("~","cyan",sep='',end="")
                            colorvariation=True
                
                mountainhere = False
                townhere = False
                
                #elif map[a][b] == 3:
                #    print("A",sep='',end="")
                
                
            print("")
        print("gold: "+str(player.gold))
        for mo in range(len(mountainList)):
            if map[mountainList[mo][0]][mountainList[mo][1]] == 2:
                print(moText[random.randint(0,2)])
        for to in range(len(qtowns)):
            if qtowns[to][0]==y and qtowns[to][1]==x:
                for i in range(len(qtowns)):
                    if qtowns[i][0]==y and qtowns[i][1]==x:
                        treasure.append([random.randint(1,48),random.randint(1,48)])
        for tr in range(len(treasure)):
            if treasure[tr][0]==y and treasure[tr][1]==x:
                player.gold+=random.randrange(30,150,5)
                for i in range(len(treasure)):
                    if treasure[i]==[y,x]:
                        treasure[i] =[-1,-1]

        
        if dir =="loc":
            print("Mountains: " + str(mountainList))
            print("Towns: "+str(townList))
            print("Treasure: " +str(treasure))
Walk(0,0)