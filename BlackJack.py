from random import randint
import os
from time import sleep


def gui():
 global game
 game=input("\nNowa gra, rozdać Karty? wpisz t: ")
 print("--------------------------------------")

def take():
  global add,card
  card=card+1
  print("\n-------------------------------")
  print("\nChcesz dobrać",card,"kartę?")
  add=input("\n t lub n: ") 

def new(x):
    os.system('cls')
    global crx,su,spc,tw
    print("losuje...")
    sleep(1)
    os.system('cls')
    print("Wylosowano: ",x)
    tw.append(x)
    su=su+x
    print("\nTY: ",tw,"suma: ",su)
    print("\nPC:  [",cpc1,',',cpc2,"] suma: ",spc)
    



def newpc():
   global spc,su
   while spc<21 and spc<=su:
     y=randint(2,8)
     spc=spc+y
     print("losuje...")
     sleep(2)
     print("\nWylosowano: ",y,"suma pc: ",spc)
     if spc>su and spc<=21:
      print("\n Przegrałeś ty masz: ",su)
      sleep(3)
      break
   if spc>21:
      print("Wygrałeś suma pc przekroczona: ",spc)
      sleep(3)
  
def startdeck():
    global tw,su,spc,cpc1,cpc2
    cr1=randint(2,8)
    cr2=randint(2,8)
    tw.append(cr1)
    tw.append(cr2)
    su=cr2+cr1
    print("\nTY: ",tw,"suma: ",su)
    cpc1=randint(2,8)
    cpc2=randint(2,8)
    spc=cpc1+cpc2
    print('\nPC:  [',cpc1,',',cpc2,'] suma: ',spc)
    take()
    
  
 
while 1==1:  
 gui()
 os.system('cls')
 card,crx,su,spc=2,0,0,0
 add="t"
 tw=[]
 startdeck()
 while su<21 and add=="t" and game=="t":
  x=randint(2,8)
  new(x)
   
  if su==21:
    print("\nWygrałeś!!! Masz Black Jacka!!")
    sleep(3)
    break
  if su>21 :
    print("\nPowyżej 21, przgrałeś")
    sleep(3)
    break
  take()
  if add=="n":
   newpc()
   break
