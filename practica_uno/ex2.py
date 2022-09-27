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
  