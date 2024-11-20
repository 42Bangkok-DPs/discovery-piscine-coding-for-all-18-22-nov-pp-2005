#!/bin/python3
import sys
import re

if len(sys.argv)==1:
    print("none")
else:
    find = re.findall("z",sys.argv[1])
    if len(find)==0:
        print("none")
    else:
        print("".join(find))
