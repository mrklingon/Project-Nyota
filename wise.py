import time
import random

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

def wisdom(num,filename):
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    qs.close()
    return quote


def getWD(fnm):
    len = file_len(fnm)
    line = wisdom(random.randrange(len),fnm)
    line = line.strip("\n");
    return ( line   )  
