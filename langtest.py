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
lang = langs[0] #first language in list

prt("Current lang: "+lang,REPL)

compthink()

def getInfo(fnm):
    len = file_len(fnm)
    line = wisdom(random.randrange(len),fnm)
    line = line.strip("\n");
    (key, val) = line.split("\", \"")
    val = val.strip('"') #remove terminal "
    val = val.strip(' "')#remove initial ' "'
    key = key.strip( '"')
    return ([key,val] )
choose = 1
quiz = 2

def createQuiz(lang):
    qdata = []
    qs = 0
    while qs < 5:
        d = getInfo(lang)
        if d not in qdata:
            qdata.append(d)
            qs = qs + 1
    return qdata
     

def doquiz(quiz):
    oops = ["wrong: ","oops: ","incorrect: "]
    wow = ["yes!","correct!","good job"]
    pixels.fill(blank)
    q = []
    while len(q) < 4:
        n = random.randrange(5)
        if not n in q:
            q.append(n)
    p = 0
    for quest in q:
        ans = random.randrange(2)
        if ans == 0:
            prt(quiz[quest][0],REPL)
            prt(str(1)+":"+quiz[quest][1],REPL)
            prt(str(2)+":"+quiz[(quest+1)%4][1],REPL)
        else:
            prt(quiz[quest][0],REPL)
            prt(str(1)+":"+quiz[(quest+1)%4][1],REPL)
            prt(str(2)+":"+quiz[quest][1],REPL)
        guess = -1
        while guess == -1:
            Val = 0
            if touch1.value:
                Val = Val +1
            if touch2.value:
                Val = Val +2

            if Val == 1 : #guess 1
                guess = 1
            if Val == 2 : #guess 2
                guess = 2
        if ans+1 == guess:
            pixels[p] = green
            prt(random.choice(wow),REPL)
        else:
            pixels[p] = red
            prt(random.choice(oops)+quiz[quest][1],REPL)
        p = p + 1
    time.sleep(3)
    pixels.fill(blank)
    prt("touch #2 for another quiz, or #1 to change language.",REPL)
    
state = choose
while True:
    Val = 0
    if touch1.value:
        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    if Val == 1 and state == choose: #advance language
        lnum = lnum + 1
        if lnum >(nlangs-1):
            lnum = 0
        compthink()
        prt("Current lang: "+langs[lnum],REPL)

    if Val == 2 and state == choose:#start quiz
        state = quiz
        newquiz = createQuiz(langs[lnum])
        doquiz(newquiz)
        state = choose    
