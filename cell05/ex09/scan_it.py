#!/bin/python3
import sys
import re

if len(sys.argv)!=3:
    print("none")
else:
    find = re.findall(sys.argv[1],sys.argv[2])
    if len(find) == 0:
        print("none")
    else:
        print(len(find))