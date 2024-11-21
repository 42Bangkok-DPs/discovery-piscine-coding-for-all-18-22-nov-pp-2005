#!/bin/python3
import sys

def shrink(str):
    print(str[0:8])

def enlarge(str):
    print(str, end="")
    for i in range(8-len(str)):
        print("Z", end="")
    print()

if len(sys.argv)==1:
    print("none")

for i in sys.argv[1:]:
    x = len(i)
    if x>8:
        shrink(i)
    elif x<8:
        enlarge(i)
    else:
        print(i)
