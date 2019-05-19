# -*- coding: utf-8 -*- 
import sys
import math
import logging
import doctest


logging.basicConfig(filename='program.log', format='%(asctime)s %(message)s',level=logging.DEBUG)


# Definição das funções 
def soma(arg1, arg2):
    """
    >>> soma(2, 2)              # testes soma
    4
    >>> soma(1, 1)
    2
    >>> soma(-2, 4)
    2
    """ 
    print(arg1 + arg2)

def subt(arg1, arg2):
    """
    >>> subt(2, 2)              # testes subtracao                  
    0
    >>> subt(10, 1)
    9
    >>> subt(-2, 4)
    -6
    """
    print(arg1 - arg2)

def mult(arg1, arg2):
    """
    >>> mult(2, 2)              # testes multiplicacao
    4
    >>> mult(10, 10)
    100
    >>> mult(-2, 4)
    -8
    """
    print(round((arg1 * arg2), 2))

def div(arg1, arg2):
    try:
        arg1 / arg2
        """
        >>> div(2, 2)               # testes divisao
        1
        >>> div(10, 2)
        5
        >>> div(2, 4)
        0.5
        """
        print(round((arg1 / arg2), 2))
    except Exception as e:                      # tratamento do erro divisor 0
        logging.exception("Exception Occurred")

def pot(arg1, arg2):
    """
    >>> pot(2, 2)               # testes potencia
    4.0
    >>> pot(10, 3)
    1000.0
    >>> pot(5, 4)
    625.0
    """
    print(round(math.pow(arg1, arg2), 2))

def mod(arg1, arg2):
    """
    >>> mod(2, 2)               # testes modulo
    0
    >>> mod(10, 3)
    1
    >>> mod(1235, 4)
    3
    """
    print(round((arg1 % arg2), 2))

def main():

    if len(sys.argv) == 4: # tamanho do array pra verificar a quantidade de argumentos
        
        # Criação de variáveis para armazenar os valores passados pelo terminal
        try:
            arg1 = float (sys.argv[1])
            arg2 = float (sys.argv[3])
            argOperador = sys.argv[2]
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
        except Exception as e:
            logging.error("Erro. os argumentos precisam ser numericos.")  # tratamento de exceção caso nao entre com numericos
    else:
        logging.error("Erro. Expressão precisa ser simples.") # tratamento de exceção caso tenha mais de 2 argumentos iniciais
    
    
    doctest.testmod()
main()
