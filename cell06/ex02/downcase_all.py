#!/bin/python3
import sys

if len(sys.argv) == 1:
    print("none")

def downcase_it():
    for i in sys.argv[1:]:
        print(i.lower())
    
downcase_it()
