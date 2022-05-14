
def cliente (informacion:dict)->dict:
    if informacion["edad"] > 18 and informacion["primer_ingreso"]==True:
        atraccion = 'X-Treme'
        total_boleta=20000*0.95
        apto=True
    elif informacion["edad"] > 18 and informacion["primer_ingreso"]==False:
        atraccion = "X-Treme"
        total_boleta=20000
        apto=True
    elif informacion["edad"] >= 15 and informacion["edad"] <= 18 and informacion["primer_ingreso"]==True:   
        atraccion = "Carros chocones"
        total_boleta=5000*0.93
        apto=True
    elif informacion["edad"] >= 15 and informacion["edad"] <= 18 and informacion["primer_ingreso"]==False:   
        atraccion = "Carros chocones"
        total_boleta=5000
        apto=True
    elif informacion["edad"] >= 7 and informacion["edad"] < 15 and informacion["primer_ingreso"]==True:
        atraccion="Sillas voladoras"
        total_boleta=10000*0.95
        apto=True
    elif informacion["edad"] >= 7 and informacion["edad"] < 15 and informacion["primer_ingreso"]==False:
        atraccion="Sillas voladoras"
        total_boleta=10000
        apto=True
    else: 
        apto=False
        atraccion="N/A"
        total_boleta="N/A"
    
    return {'nombre':informacion["nombre"],'edad': informacion["edad"],'atraccion':atraccion,'apto':apto,'primer_ingreso':informacion["primer_ingreso"],'total_boleta':total_boleta}
 
    
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
}
print(cliente(informacion))


'''
{'nombre': 'Johana Fernandez', 'edad': 20, 'atraccion': 'X-Treme', 'apto': True, 'primer_ingreso': True, 'total_boleta': 19000.0}
{'nombre': 'Johana Fernandez', 'edad': 20, 'atraccion': 'X-Treme', 'apto': True, 'primer_ingreso': True, 'total_boleta': 19000.0}
{'nombre': 'Johana Fernandez', 'edad': 20, 'atraccion': 'X-Treme', 'apto': True, 'primer_ingreso': True, 'total_boleta': 19000.0}


'''