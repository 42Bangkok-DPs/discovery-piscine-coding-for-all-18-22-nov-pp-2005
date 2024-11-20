#!/bin/python3
import sys

if len(sys.argv)!=2:
    print("none")
else:
    user = input("What was the parameter? ")
    if user == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")