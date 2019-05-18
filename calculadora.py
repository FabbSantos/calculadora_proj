# -*- coding: utf-8 -*- 
import sys
import math

# Criação de variáveis para armazenar os valores passados pelo terminal
arg1 = float (sys.argv[1])
arg2 = float (sys.argv[3])
argOperador = sys.argv[2]

# Definição das funções 
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
    if argOperador == '+':
       soma(arg1, arg2)
    elif argOperador == '-':
        subt(arg1, arg2)
    elif argOperador == '*':
        mult(arg1, arg2)
    elif argOperador == '/':
        div(arg1, arg2)
    elif argOperador == '**':
        pot(arg1, arg2)
    elif argOperador == 'mod':
        mod(arg1, arg2)
    else: 
        print("Erro: Operação inválida.")

main()