#importar las librerias a usar
import sys
import math

#crear la funcion que genere un arreglo con la lista de numeros que se asigne desde el input en consola
def crear_arr():
    return list(range(1,int(sys.argv[1])+1)) 

#crear la funcion para saber si es primo o no...  
def es_primo(arr):
    primos = [] 
    for num in arr: #revisar cada numero del arreglo
        if num != 1: #uno, no es primo
            n = math.floor(math.sqrt(num)) #revisar los factores que sean menor a la raíz cuadrada del numero
            primo = True #bool si es primo
            for i in range(2,n+1): #revisar los factores
                if num % i == 0: #si el modulo es cero, no es primo
                    primo = False #bool en falso
                    break #termina el ciclo
            if primo:#si es primo se suma a la lista de primos totales en el arreglo
                primos.append(num)
    return primos #return la lista de primos
    
arr_entrada = crear_arr() #arreglo de num
print(len(es_primo(arr_entrada))) #arreglo de primos
print(arr_entrada) #arreglo completo


#codigo 2 es para una entrada de numeros definidos... funciona pero no es la actividad asignada
'''
import sys

#Funcion para saber si es primo o no. Si es primo lo pone como TRUE si no es primo el resultado es FALSE
def es_primo(numero): 
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

n = len(sys.argv) #Array de las variables a analizar, estas se llaman desde la terminal, ejemplo: python3 ex2.py 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
for i in range(1, n):
    print(i, es_primo(i))
'''
  