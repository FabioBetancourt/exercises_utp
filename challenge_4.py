
def ordenes(rutinaContable):
    from functools import reduce
    mult=list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2] , x[1:] )), rutinaContable))
    total= list(map(lambda x: [x[0]] + [reduce(lambda a,b:a+b , x[1:])], mult)) 
    total = list(map(lambda x: x if x[1] >= 600000 else [x[0], x[1]+ 25000]  ,total))
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in total:
        print(f'La factura {i[0]} tiene un total en pesos de {i[1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')
    
ordenes([
 [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
 [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
 [6591, ("7812", 2, 11.99), ("9652",11,18.99)]]
)

