def AutoPartes(agenda: list):
    ventas={} #Inicializar diccionario
    for IdProducto,dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta in agenda:   #Ciclo para agregar un nuevo evento
        if ventas.get(IdProducto ) == None:             #Fuerza la entrada
            ventas[IdProducto ] = []                    #Creacion de un nuevo evento
        ventas[IdProducto ].append((dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta))  #Registro de una nueva lista de tuplas en el dict ventas
    return ventas


def consultaRegistro(ventas, idproducto): 
    partlog=''
    if idproducto in ventas.keys():
        for values in ventas[idproducto]:
            partlog +='Producto consultado : '+str(idproducto)+'  Descripción  '+str(values[0])+'  #Parte  '+str(values[1])+'  Cantidad vendida  '+str(values[2])+'  Stock  '+str(values[3])+'  Comprador '+str(values[4])+'  Documento  '+str(values[5])+'  Fecha Venta  '+str(values[6])
            print(partlog)
    else:
        print ("No hay registro de venta de ese producto")


consultaRegistro(AutoPartes([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]),2010) 