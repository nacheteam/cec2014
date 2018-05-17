import cec2014

def getFunciones():
    '''
    @brief Función que devuelve una lista con las 20 funciones implementadas.
    @return Devuelve un vector con las funciones.
    '''
    return [f1, f2, f3, f4, f5 , f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]

def getNumFunciones():
    '''
    @brief Función que devuelve el número de funciones implementadas.
    @return Devuelve 20 que es el número de funciones cec implementadas.
    '''
    return 20

def getLimInf():
    '''
    @brief Función que devuelve el límite inferior de cada componente del vector de soluciones.
    @return -100 es el límite inferior.
    '''
    return -100

def getLimSup():
    '''
    @brief Función que devuelve el límite superrior de cada componente del vector de soluciones.
    @return 100 es el límite inferior.
    '''
    return 100

def getFuncMinValor(i):
    '''
    @brief Función que devuelve el valor mínimo de la función.
    @param i Función i-ésima de la que se quiere obtener su mínimo valor.
    @return Devuelve el valor mínimo de la función
    '''
    return i*100

def getInfo(i):
    '''
    @brief Función que da la información del límite inferior, superior y el mínimo valor de la función que queramos.
    @param i Función i-ésima de la que queremos obtener información
    @retur Devuelve un diccionario con los campos inf, sup y minimo con los datos del valor inferior de cada componente, el valor superior y el valor mínimo de la función.
    '''
    return {'inf': getLimInf(), 'sup': getLimSup(), 'minimo': getFuncMinValor(i)}

################################################################################
##                      IMPLEMENTACIÓN DE FUNCIONES CEC                       ##
################################################################################


def f1(x):
    return cec2014.cec14(x,1)

def f2(x):
    return cec2014.cec14(x,2)

def f3(x):
    return cec2014.cec14(x,3)

def f4(x):
    return cec2014.cec14(x,4)

def f5(x):
    return cec2014.cec14(x,5)

def f6(x):
    return cec2014.cec14(x,6)

def f7(x):
    return cec2014.cec14(x,7)

def f8(x):
    return cec2014.cec14(x,8)

def f9(x):
    return cec2014.cec14(x,9)

def f10(x):
    return cec2014.cec14(x,10)

def f11(x):
    return cec2014.cec14(x,11)

def f12(x):
    return cec2014.cec14(x,12)

def f13(x):
    return cec2014.cec14(x,13)

def f14(x):
    return cec2014.cec14(x,14)

def f15(x):
    return cec2014.cec14(x,15)

def f16(x):
    return cec2014.cec14(x,16)

def f17(x):
    return cec2014.cec14(x,17)

def f18(x):
    return cec2014.cec14(x,18)

def f19(x):
    return cec2014.cec14(x,19)

def f20(x):
    return cec2014.cec14(x,20)
