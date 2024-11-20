#!/bin/python3
import sys

if len(sys.argv) == 1:
    i=0
    while i<11:
        print(f"Teble de {i}:", end=" ")
        j=0
        while j<11:
            print(i*j, end=" ")
            j+=1
        print()
        i+=1
else:
    print("none")