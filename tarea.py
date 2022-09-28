from asyncore import read
from cgi import print_arguments
from decimal import DivisionUndefined
from msilib.schema import tables
from operator import truediv
from re import T
from turtle import pen
from unicodedata import east_asian_width
from xml.dom import NoModificationAllowedErr

#Linea de codigo para la suma, resta, multiplicacion y division

print ("ingrese su primer numero")
n1 = int(input())
print ("ingrese su segundo numero")
n2 = int(input())
suma =  n1 + n2
resta = n1 - n2   #operacion
multi = n1 * n2
divi = n1 / n2

#impresion de resultados

print ("La suma es:",suma)
print ("La resta es:",resta)
print ("La multiplicacion  es:",multi)
print ("La divicion es:",divi)

#Linea de codigo para realizar la verificacion de numero primo
         
n = int(input("ingresar un numero para saber si es primo: "))
x = 1
c = 0
while x <= n:
    if n % x == 0:  #operacion
        c = c + 1
    x = x + 1
if c == 2:

#impresion de resultados

    print("El numero ingresado: ",n,"es primo")
else:
    print("El numero ingresado: ",n,"no es primo")

#Linea de codigo para realizar la verificacion de un numero palindromo

pali = int(input("ingrese 3 digitos de numeros para saber si es palindromo"))
if pali > 99 and pali < 1000:
    a = pali // 100   #operacion
    b = pali % 10
    if a == b:

#impresion de resultados

        print("El numero ingresado: ",pali,"es palindromo")
    else:
        print("El numero ingresado: ",pali,"no es palindromo")