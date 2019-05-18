# -*- coding: utf-8 -*- 
import sys
import math

if sys.argv[2] == '+':
    output = float(sys.argv[1]) + float(sys.argv[3])
    print (output)
elif sys.argv[2] == '-':
    output = float(sys.argv[1]) - float(sys.argv[3])
    print(output)
elif sys.argv[2] == '*':
    output = float(sys.argv[1]) * float(sys.argv[3])
    print (round(output, 2))
elif sys.argv[2] == '/':
    output = float(sys.argv[1]) / float(sys.argv[3])
    print (round(output, 2))