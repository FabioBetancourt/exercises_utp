def AutoPartes(ventas: list):
    ventas={} #Inicializar diccionario
    for IdProducto,dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta in ventasg:         #Ciclo para agregar un nuevo evento
        if ventas.get(IdProducto) == None:             #Fuerza la entrada
            ventas[IdProducto] = []                    #Creacion de un nuevo evento
        ventas[IdProducto].append((dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta))  #Registro de una nueva lista de tuplas en el dict agenda
    return ventas

def consultaRegistro(ventas, idproducto): 
    AutoPartes()
    if idproducto == 2010:
        print ('Producto consultado : {idProducto} Descripción {dProducto} #Parte {pnProducto} Cantidad vendida {cvProducto} Stock {sProducto} Comprador {nComprador} Documento {cComprador} Fecha Venta {fVenta}')
    elif idproducto == 9852:
       print ('Producto consultado : {idProducto} Descripción {dProducto} #Parte {pnProducto} Cantidad vendida {cvProducto} Stock {sProducto} Comprador {nComprador} Documento {cComprador} Fecha Venta {fVenta}')
    else:
        print ("No hay registro de venta de ese producto")


#Producto consultado : 2010 Descripción bujía #Parte MS9512 Cantidad vendida 4 Stock 15 Comprador Carlos Rondon Documento 1256 Fecha Venta 12/06/2020
#Producto consultado : 2010 Descripción bujía #Parte ER6523 Cantidad vendida 9 Stock 36 Comprador Pedro Montes Documento 1243 Fecha Venta 12/06/2020

#Producto consultado : 2010 Descripción bujía #Parte MS9512 Cantidad vendida 4 Stock 15 Comprador Carlos Rondon Documento 1256 Fecha Venta 12/06/2020
#Producto consultado : 2010 Descripción bujía #Parte ER6523 Cantidad vendida 9 Stock 36 Comprador Pedro Montes Documento 1243 Fecha Venta 12/06/2020


ventasg=([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')])



consultaRegistro(AutoPartes(ventasg), 9852)
