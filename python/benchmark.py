import cec2014

class Benchmark:

    num_funciones = 20
    inf = -100
    sup = 100

    def getFunciones(self):
        '''
        @brief Función que devuelve una lista con las 20 funciones implementadas.
        @return Devuelve un vector con las funciones.
        '''
        return [lambda x: cec2014.cec14(x,i) for i in range(1,self.num_funciones+1)]

    def getNumFunciones(self):
        '''
        @brief Función que devuelve el número de funciones implementadas.
        @return Devuelve 20 que es el número de funciones cec implementadas.
        '''
        return self.num_funciones

    def getLimInf(self):
        '''
        @brief Función que devuelve el límite inferior de cada componente del vector de soluciones.
        @return -100 es el límite inferior.
        '''
        return self.inf

    def getLimSup(self):
        '''
        @brief Función que devuelve el límite superrior de cada componente del vector de soluciones.
        @return 100 es el límite inferior.
        '''
        return self.sup

    def getFuncMinValor(self,i):
        '''
        @brief Función que devuelve el valor mínimo de la función.
        @param i Función i-ésima de la que se quiere obtener su mínimo valor.
        @return Devuelve el valor mínimo de la función
        '''
        return i*100

    def getInfo(self,i):
        '''
        @brief Función que da la información del límite inferior, superior y el mínimo valor de la función que queramos.
        @param i Función i-ésima de la que queremos obtener información
        @return Devuelve un diccionario con los campos inf, sup y minimo con los datos del valor inferior de cada componente, el valor superior y el valor mínimo de la función.
        '''
        return {'inf': self.getLimInf(), 'sup': self.getLimSup(), 'minimo': self.getFuncMinValor(i)}

    def getFuncion(self,i):
        '''
        @brief Función que devuelve la función objetivo i-ésima.
        @param i Función i-ésima a devolver.
        @return Devuelve la función i-ésima del Benchmark.
        '''
        return self.getFunciones()[i]
