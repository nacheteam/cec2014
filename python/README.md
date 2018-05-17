# cec2014

Wrapper de las funciones objetivo de CEC2014.
Hecho por [@nacheteam](https://github.com/nacheteam) y [@mx_psi](https://github.com/mx-psi/), inspirado en la [versión para CEC2013](https://github.com/dmolina/cec2013lsgo) de [@dmolina](https://github.com/dmolina).

El código original ha sido obtenido de:

> Liang, J. J., Qu, B. Y., & Suganthan, P. N. (2013). [Problem definitions and evaluation criteria for the CEC 2014 special session and competition on single objective real-parameter numerical optimization.](http://web.mysites.ntu.edu.sg/epnsugan/PublicSite/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2fepnsugan%2fPublicSite%2fShared%20Documents%2fCEC%2d2014&FolderCTID=&View=%7bDAF31868%2d97D8%2d4779%2dAE49%2d9CEC4DC3F310%7d) *Computational Intelligence Laboratory, Zhengzhou University, Zhengzhou China and Technical Report, Nanyang Technological University, Singapore.*

# Requisitos e Instalación

Los requisitos necesarios son:

- Python 3 (probado con Python 3.5.2)
- Cython 3 (probado con Cython 0.28.2)
- NumPy (probado con NumPy 1.14.1)

En distribuciones derivadas de Debian como Ubuntu ejecuta `make debian-install` como administrador para instalar las dependencias necesarias. En otras distribuciones necesitas instalar manualmente Cython y el paquete de desarrollo de Python 3.

Ejecuta `make build` para crear la librería.

# Uso

Utiliza la clase `Benchmark` del módulo `benchmark` para obtener cada función así como su valor óptimo e información asociada.

Alternativamente puedes utilizar directamente el módulo `cec2014` que exporta la función `cec14(x,i)`.
Esta función evalúa un array de NumPy `x` respecto de la función objetivo número `i`.

**Importante:** un fallo en las dimensiones o en el tipo de los elementos (deben ser `float`) provocará un error irrecuperable.


