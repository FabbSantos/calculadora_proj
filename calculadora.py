# -*- coding: utf-8 -*- 
import sys

if sys.argv[2] == '+':
    output = float(sys.argv[1]) + float(sys.argv[3])
    print (output)
elif sys.argv[2] == '-':
    output = float(sys.argv[1]) - float(sys.argv[3])
    print(output)