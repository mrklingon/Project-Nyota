import time
import random
import neopixel
import board
import touchio
from prt import *
from wise import *

# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


#Define colors
pink = (12,10,12)
gold = (50, 40, 5)
blue = (0,0,8)
orange = (25, 10, 0)
blank = (0,0,0)
grn = (0,20,0)
green  = (0,20,0)
red = (20,0,0)
paleblue = (0,0,1)
white = (20,20,20)
purple = (20,0,30)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)
colors = [pink,gold,blue,orange,green,red,paleblue,white,purple]
REPL=True
def docolor(color): #show a color  briefly
    for i in range(4):
        pixels[i] = color


    pixels.show()
    time.sleep(.25)

    for i in range(4):
        pixels[i] = blank

    pixels.show()


def blinknum(num,color): #count out a number in a color
    for i in range(num):
        docolor(color)
        time.sleep(.25)



def compthink(): #blink out all the colors when computer "thinking"
    for clr in colors:
        blinknum(1,clr)

if REPL == False:
    stoplight = [red,gold,green]
    for i in range(3):
        blinknum(1+i,stoplight[i])
        

nlangs = file_len("langs")
prt (("number of languages: "+str(nlangs)),REPL)
lnum = 0
langs = []
for i in range(nlangs):
    lname = wisdom(i,"langs")
    lname = lname.strip("\n")
    prt (lname,REPL)
    langs.append(lname)
lang = langs[0]
#set up pixels

prt("Current lang: "+lang,REPL)

compthink()

def getWD(fnm):
    len = file_len(fnm)
    line = wisdom(random.randrange(len),fnm)
    line = line.strip("\n");
    (key, val) = line.split("\", \"")
    val = val.strip('"') #remove terminal "
    val = val.strip(' "')#remove initial ' "'
    key = key.strip( '"')
    return (key+" : " +val     )


while True:
    Val = 0
    if touch1.value:
        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    if Val == 1: #advance language
        lnum = lnum + 1
        if lnum >(nlangs-1):
            lnum = 0
        compthink()
        prt("Current lang: "+langs[lnum],REPL)

    if Val == 2 : #display words
        blinknum(1,blue)
        for i in range(5):
            prt(getWD(langs[lnum]),REPL)
    time.sleep(.25)

