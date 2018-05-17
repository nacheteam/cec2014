# cec2014

Wrapper de las funciones objetivo de CEC2014.
Hecho por [@Bruno-sm](https://github.com/Bruno-sm).

El código original ha sido obtenido de:

> Liang, J. J., Qu, B. Y., & Suganthan, P. N. (2013). [Problem definitions and evaluation criteria for the CEC 2014 special session and competition on single objective real-parameter numerical optimization.](http://web.mysites.ntu.edu.sg/epnsugan/PublicSite/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2fepnsugan%2fPublicSite%2fShared%20Documents%2fCEC%2d2014&FolderCTID=&View=%7bDAF31868%2d97D8%2d4779%2dAE49%2d9CEC4DC3F310%7d) *Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou China and Technical Report, Nanyang Technological University, Singapore.*


## Compilación 
Ejecuta `make` para compilar la librería. Esta se guardará en la carpeta libs, eres libre de cambiar el nombre de la librería y la localización en el Makefile, pero asegurate de modificar de forma apropiada la linea 3 de [cec14\_func.jl](https://github.com/nacheteam/cec2014/tree/master/julia/src/cec14_func.jl).


## Uso
Incluye el archivo [cec14\_func.jl](https://github.com/nacheteam/cec2014/tree/master/julia/src/cec14_func.jl) donde quieras usar las funciones del cec.

```julia
include("cec14_func.jl")
```

En él se proporcionan dos funciones:

- **cec14_func_eval:**
  Evalúa un punto sobre la función del cec que quieras
  ```julia
  # Evalúa el punto (0, 0) sobre la primera función del cec.
  cec14_func_eval(1, [0,0]) # 3.279714013173407e8
  ```
  
- **cec14_func:**
  Devuelve la función del cec que quieras
  ```julia
  # Primera función del cec.
  f = cec14_func(1)
  # Evalúa la función en el (0, 0)
  f([0,0]) # 3.279714013173407e8
  ```
  

## Observaciones
- Es importante que la carpeta cec2014\_data esté en el mismo directorio desde el que vayas a ejecutar el programa.

- Los límites de búsqueda para todas las funciones son \[-100, 100\] (en la dimensión correspondiente)

- El óptimo de las funciones es 100\*número\_función. Es decir 100 para la primera función, 200 para la segunda, etc.

- El óptimo se alcanza en el punto guardado en cec2014\_data/shift\_data\_x.txt donde x es el número de la función.

- La dimensión debe ser 2, 10, 20, 30, 50 o 100.


## Contribuciones
Sientete libre de proponer cualquier mejora, siempre son bienvenidas.
