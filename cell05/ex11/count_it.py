#!/bin/python3
import sys

arg = len(sys.argv)
if arg==1:
    print("none")
else:
    print(f"parameters: {arg-1}")
    for i in range(1,arg):
        print(f"{sys.argv[i]} {len(sys.argv[i])}")