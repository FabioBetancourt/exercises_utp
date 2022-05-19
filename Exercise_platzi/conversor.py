# Conversos de moneda de pesos colombianos a dolares

def conversor(pesos,valor_dolar):
    pesos = float(input("Cuantos pesos " +pesos+ " a convertir: "))
    dolares= round(pesos/valor_dolar,2)
    print("Tienes " + str(dolares) + " Dolares 🤑🤑")

menu="""Bienvenido al conversor de monedas 💵
1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos
Elige una opcion: """
opcion=input(menu)

if opcion == '1':
    conversor("Colombianos",4050)
elif opcion == '2':
    conversor("Argentinos",65)
elif opcion == '3':
    conversor("Mexicanos",24)
else:
    print("Ingrese una opcion correcta 😒")




