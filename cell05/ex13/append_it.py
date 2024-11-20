#!/bin/python3
import sys

if len(sys.argv)==1:
    print("none")
else:
    for i in sys.argv[1:]:
        if not i.endswith("ism"):
            print(i+"ism")
