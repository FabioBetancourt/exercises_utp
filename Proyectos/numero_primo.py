import math
def run():
    numero=int(input("Ingrese un numero: "))
    if es_primo(numero):
        print("Es primo")
    else: 
        print("No es primo")

def es_primo(numero):
    if numero == 1:
        return False
    if numero == 0:
        print("Tiene que ser mayor que cero")
    for i in range(1,numero+1):
        if (math.factorial(i-1)+1) % i == 0:
            return True
        else:
            return False
    
    


# def es_primo(numero):
#     if numero == 1:
#         return False
#     else:
#         contador=0
#     for i in range(1,numero+1):
#         if i==1 or i==numero:
#             continue
#         if numero % i == 0 :
#             contador +=1
#     if contador == 0:
#         return True
#     else:
#         return False
            



if __name__ == '__main__':
    run()
    