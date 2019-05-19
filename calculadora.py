# -*- coding: utf-8 -*- 
import sys
import math
import logging

# Criação de variáveis para armazenar os valores passados pelo terminal
arg1 = float (sys.argv[1])
arg2 = float (sys.argv[3])
argOperador = sys.argv[2]

logging.basicConfig(filename='program.log', format='%(asctime)s %(message)s',level=logging.DEBUG)


# Definição das funções 
def soma(arg1, arg2):
    print(arg1 + arg2)

def subt(arg1, arg2):
    print(arg1 - arg2)

def mult(arg1, arg2):
    print(round((arg1 * arg2), 2))

def div(arg1, arg2):
    try:
        arg1 / arg2
        print(round((arg1 / arg2), 2))
    except Exception as e:                      # tratamento do erro divisor 0
        logging.exception("Exception Occurred")

def pot(arg1, arg2):
    print(round(math.pow(arg1, arg2), 2))

def mod(arg1, arg2):
    print(round((arg1 % arg2), 2))

def main():
    if len(sys.argv) == 4:   # tamanho do array pra verificar a quantidade de argumentos
        logging.info('Calculator app started with values: %.2f e %.2f', arg1, arg2) # log mostrando os valores iniciais
        try:
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
            elif argOperador == 'mod' or argOperador == '%':
                mod(arg1, arg2)
            else: 
                print("Erro: Operação inválida.")
        except Exception as e:
            logging.exception("Exception Occurred")
    else:
        logging.exception("Exception Occurred. Expressão precisa ser simples.") # tratamento de exceção caso tenha mais de 2 argumentos iniciais
main()
