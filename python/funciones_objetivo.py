import cec2014

def getFunciones():
    '''
    @brief Función que devuelve una lista con las 20 funciones implementadas.
    @return Devuelve un vector con las funciones.
    '''
    return [lambda x: cec2014.cec14(x,i) for i in range(1,21)]

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
    @return Devuelve un diccionario con los campos inf, sup y minimo con los datos del valor inferior de cada componente, el valor superior y el valor mínimo de la función.
    '''
    return {'inf': getLimInf(), 'sup': getLimSup(), 'minimo': getFuncMinValor(i)}

def getFuncion(i):
    '''
    @brief Función que devuelve la función objetivo i-ésima.
    @param i Función i-ésima a devolver.
    @return Devuelve la función i-ésima del Benchmark.
    '''
    return getFunciones()[i]
