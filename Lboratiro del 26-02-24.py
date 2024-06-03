# -*- coding: utf-8 -*-
"""Funciones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tl0lMaEZ58ldFUjDhcLSGvkUnhu8C4JC

Estudiantes:

*  Jimena Barrantes Zuñiga
*  Nahomy Álvarez Quesada
*  Nicole Calderon Sequeira
*  Monica Nacarado Dengo
*  Ezequiel Duarte Balmaceda

#   Circulo
"""

import math

def calcular_area_circulo(radio):
  return math.pi * radio**2

def calcular_perimetro_circulo(radio):
  return 2*math.pi * radio


radio= int(input("Digite el valor del radio: "))

area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)
print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Cuadrado"""

import math

def calcular_area_cuadrado(lado):
  return lado * lado

def calcular_perimetro_cuadrado(lado):
  return 4 * lado

lado= int(input("Digite un valor:"))
area=calcular_area_cuadrado(lado)
perimetro=calcular_perimetro_cuadrado(lado)
print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Plígono regular(Hexagono)"""

import math

def calcular_perimetro_poligno(perimetro, apotema):
  return 6 * lado
def calcular_area_poligno(lado):
  return (perimetro*apotema)/2



lado= int(input("Digite el valor de uno de los lados del poligono:"))
lado= int(input("Digite el valor de la apotema"))
perimetro=calcular_perimetro_cuadrado(lado)
area=calcular_area_cuadrado(lado)

print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Triangulo Equilatero"""

import math

def calcular_area_triangulo_Equi(lado):
  return ((lado**2)*math.sqrt(3))/4

def calcular_perimetro_triangulo_Equi(lado):
  return 3 * lado

lado= int(input("Digite un valor de uno de los lados del triangulo:"))
area=calcular_area_triangulo_Equi(lado)
perimetro=calcular_perimetro_triangulo_Equi(lado)
print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Rectángulo"""

import math

def calcular_area_rectangulo(base, altura):
  return base * altura

def calcular_perimetro_rectangulo(base, altura):
  return 2*base+2*altura

base= int(input("Digite un valor para la base:"))
altura= int(input("Digite un valor para la altura:"))
area=calcular_area_rectangulo(base, altura)
perimetro=calcular_perimetro_rectangulo(base, altura)
print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Rombo"""

import math

def calcular_area_rombo(D,d):
  return (D*d / 2)

def calcular_perimetro_rombo(lado):
  return 4 *lado

D= int(input("Diagonal mayor:"))
d=int(input("Diagnal menor:"))
lado= int(input("Lado:"))

area=calcular_area_rombo(D,d)
perimetro=calcular_perimetro_rombo(lado)

print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Trapecio"""

import math

def calcular_area_trapecio(B,b,h):
  return ((B+b) / 2)*h

def calcular_perimetro_trapecio(lado):
  return 4 *lado

B= int(input("Base Mayor:"))
b=int(input("Base Menor:"))
h=int(input("Altura:"))
lado= int(input("Lado:"))

area=calcular_area_trapecio(B,b,h)
perimetro=calcular_perimetro_trapecio(lado)

print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Paralelogramo"""

import math

def calcular_area_paralelogramo(base, altura):
  return base * altura

def calcular_perimetro_paralelogramo(lado, base):
  return 2*lado+2*base

base= int(input("Digite un valor para la base:"))
altura= int(input("Digite un valor para la altura:"))
lado= int(input("Digite un valor para el lado:"))
area=calcular_area_paralelogramo(base, altura)
perimetro=calcular_perimetro_paralelogramo(lado, base)
print("El area es: ",area)
print("El perimetro: ", perimetro)

"""# Triangulo"""

import math

def calcular_area_triangulo(base, altura):
  return (base*altura)/2

def calcular_perimetro_trangulo(lado1,lado2,lado3):
  return lado1+lado2+lado3

print("Ingrese la base del triangulo: ")
base= int(input("Digite un valor para la base: "))

print("Ingrese la altura del triangulo: ")
altura= int(input("Digite un valor para la altura: "))

print("Ingrese el lado1 del triangulo: ")
lado1= int(input("Digite un valor para el lado1: "))
print("Ingrese el lado2 del triangulo: ")
lado2= int(input("Digite un valor para el lado2: "))
print("Ingrese el lado3 del triangulo: ")
lado3= int(input("Digite un valor para el lado3: "))

area= calcular_area_triangulo(base, altura)
perimetro= calcular_perimetro_trangulo(lado1,lado2,lado3)

print("El area es: ",area)
print("El perimetro: ", perimetro)