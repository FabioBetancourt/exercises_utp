'''
Una entidad Bancaria o entidad financiera, requiere calcular
el valor de los intereses ganados y el total final de dinero para diferentes clientes, de
acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un
producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo
determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece
rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo
determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira
antes de este periodo se aplica una penalidad del 2%.
En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos
meses se determina a través de la siguiente formula:
'''
def CDT (usuario, capital, tiempo):
    if tiempo > 2 :
        valor_inte=(capital*0.03*tiempo)/12
        valor_total=valor_inte+capital
        return print("Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total))
    else:
        valor_per=int(capital)*0.02
        valor_total=int(capital)-valor_per
        return print("Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total))
        
CDT("AB1012", 1000000, 3)
CDT("ER3366", 650000, 2)


