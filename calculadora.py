# -*- coding: utf-8 -*- 
import sys
import math
arg1 = sys.argv[1]
arg2 = sys.argv[3]
def soma(arg1, arg2):
    print(arg1 + arg2)

def subt(arg1, arg2):
    print(arg1 - arg2)

def mult(arg1, arg2):
    print(round((arg1 * arg2), 2))

def div(arg1, arg2):
    print(round((arg1 / arg2), 2))

def pot(arg1, arg2):
    print(round(math.pow(arg1, arg2), 2))

def mod(arg1, arg2):
    print(round((arg1 % arg2), 2))

def main():
    if sys.argv[2] == '+':
       soma(arg1, arg2)
    elif sys.argv[2] == '-':
        subt(arg1, arg2)
    elif sys.argv[2] == '*':
        mult(arg1, arg2)
    elif sys.argv[2] == '/':
        div(arg1, arg2)
    elif sys.argv[2] == '**':
        pot(arg1, arg2)
    elif sys.argv[2] == 'mod':
        mod(arg1, arg2)
    else: print("Erro: Operação inválida.")
main()