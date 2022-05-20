
import random

def run():
    numero_aleatorio = random.randint(0 , 100)
    numero_escogido = int(input("Escribe un numero del 1 al 100: "))
    while numero_escogido != numero_aleatorio:
        if numero_escogido < numero_aleatorio:
            print("busque un numero mas grande: ")
        else: 
            print("busque un numero mas pequeño: ")
        numero_escogido = int(input("Escribe otro numero: "))
    print("Ganaste!")
        


if __name__ == '__main__':
    run()
    