'''
Created on 9 de mar de 2017

@author: Carlos Cesar (cesarcarlosfreitas@gmail.com)
'''
from math import log

number = int(input("tamanho da mensagem? "))
bits = int(log(number, 2) + 1)
print("Quamtidade de bit = {0}".format(bits))