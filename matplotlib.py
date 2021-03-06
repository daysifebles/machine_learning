# -*- coding: utf-8 -*-
"""matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xzqvWDyz0Rvq6qafFCTIoU6a40a_sk-w

# MATPLOTLIB

Para visualización de datos.
"""

import matplotlib.pyplot as plt
import numpy as np

"""## Función `plot()`"""

#help(plt.plot)
#Crear un gráfico sensillo, solo pasandole los valores del eje Y.

plt.plot([1, 2, 3, 4])

#Si al comando plot se le pasa una sola lista por defecto la toma como los valores
#en el eje Y. Por defecto para el eje X toma la lista [0,1,2,3,...], este tiene el
#mismo tamaño que la lista introducida para el eje Y.

plt.ylabel('Algunos números') #colocar nombre al eje y

plt.show() #Para finalmente mostrar el gráfico.

#En esta parte se le pasarán dos listas que corresponden a las coordenadas de los ejes, y también se 
#utilizará el parámetro 'fmt'.

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

#La primera lista corresponde a los valores en el eje X, la segunda al eje Y y el último parámetro de forma.
#El formato para este parámetro es '[marker][line][color]' forma del punto,forma de la línea y el color.

plt.axis([0,6,0,20]) 

#Este último comando es para especificar los límites de los ejes [xmin, xmax, ymin, ymax] 

plt.ylabel('Algunos Números')
plt.show()

"""### Parámetro `fmt`

A continuación se mostrarán algunas de las opciones del parámetro `fmt`, recordemos que el formato es el siguiente `[marker][line][color]`.

*  `marker`: Forma del punto.

|  Simbolo  |  Descripción   |
|:---------:|:--------------:|
|  ``'.'``  | Punto |
|  ``','``  | Punto del tamaño de un pixel |
|  ``'o'``  | Círculo |
|  ``'v'``  | Triángulo hacia abajo |
|  ``'^'``  | Triángulo hacia arriba |
|  ``'<'``  | Triángulo izquierda |
|  ``'>'``  | Triángulo derecho |
|  ``'1'``  | tri_bajo |
|  ``'2'``  | tri_arriba |
|  ``'3'``  | tri_izquierda |
|  ``'4'``  | tri_derecha |
|  ``'s'``  | cuadro |
|  ``'p'``  | Pentágono |
|  ``'*'``  | Estrella |
|  ``'h'``  | Hexagono1 |
|  ``'H'``  | Hexagono2 |
|  ``'+'``  | Símbolo de suma + |
|  ``'x'``  | Símbolo x |
|  ``'D'``  | Diamante |
|  ``'d'``  | Diamante más delgado |
|  ``'\|'``  | Línea vertical |
|  ``'_'``  | Línea horizontal |

*  `line` : Estilo de línea.
   
|  Simbolo  |  Descripción   |
|:---------:|:--------------:|
|  ``'-'``  | Línea solida |
|  ``'--'`` | Línea rayada |
|  ``'-.'`` | Línea y punto |
|  ``':'``  | Línea de dos punto continuos |

*  `color`: Color de las líneas o puntos.

|  Simbolo  |  Descripción   |
|:---------:|:--------------:|
| ``'b'``   | Azul |
| ``'g'``   | Verde |
| ``'r'``   | Rojo |    
| ``'c'``   | Cyan |       
| ``'m'``   | Magenta |
| ``'y'``   | Amarillo |   
| ``'k'``   | Negro |        
| ``'w'``   | Blanco |  

Se pueden hacer combinaciones con todos estos simbolos.

### Más de dos líneas en un gráfico

Con la función `plot()` podemos realizar un único gráfico que contenga dos o más líneas.
"""

# Vamos a utilizar la libreria numpy para generar secuencias de números.

import numpy as np

#Con la función arange(), que vamos usar a continuación, de la libreria que acabamos
#de cargar construiremos un arreglo con los valores entre 0 y 5 con un salto de 0.2. 
t = np.arange(0., 5., 0.2) 
t

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') 
# 'r--' rojo de líneas, 'bs' azul cuadros y 'g^' verde de triángulos
plt.show()

"""## Función `scatter()`

En esta sección se contruira un gráfico usando una base de datos. Para este ejemplo un diccionario.

Usaremos la función `scatter()` que permite realizar gráficos variando el tamaño y el color de los puntos
"""

#Para esta sección vamos a generar un diccionario con tres listas.
data = {'a': np.arange(50), #rango entre 0 y 50 con un salto de 1
        'c': np.random.randint(0, 50, 50), #50 números aleatorios entre 0 y 50 enteros
        'd': np.random.randn(50)}# 50 números aleatorios normales
data['b'] = data['a'] + 10 * np.random.randn(50) #generar una nueva llave para el diccionario
data['d'] = np.abs(data['d']) * 100 #abs() da el valor adsoluto de los datos guardados en d
data

plt.scatter('a', 'b', c='c', s='d', data=data)
# c=color y s=tamaño del punto

plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

"""## Gráfico de barras y varios gráficos en uno

Para los gráficos de barra se usa la función `bar()`.

Para generar un gráfico que contenga más de dos gráficos se usa la función `figure()` para un gráfico con tamaño específico y con la función `subplot()` se especifica el gráfico que se le ira agregando.
"""

#Para este ejemplo supongamos que tenemos empresas que venden cierto artículo,
#y que tenemos la cantidad de artículos vendidos en el último año.

empresas = ['Empresa_A', 'Empresa_B', 'Empresa_C']
ventas_anuales = [1253, 2580, 500]

plt.figure(figsize=(10, 3))
#La función figure() genera una nueva imagen
#figsize ancho y largo en inches.

#dentro de esta fígura vamos a guardar tres figuras, para ello usaremos la función
#subplot()
plt.subplot(131) #número de filas, número de columnas, número del gráfico
plt.bar(empresas,ventas_anuales)

plt.subplot(132)
plt.scatter(empresas,ventas_anuales) #gráfico de punto

plt.subplot(133)
plt.plot(empresas,ventas_anuales) #gráfico de línea

plt.suptitle('Gráfico de categorias')
plt.show()

"""## Uso de funciones en gráficos

Se definirá una función para generar valores y ésta se usara dentro de la función `plot()` para generar los valores de un cierto eje.

La función que crearemos es la siguiente

$$f(t) = e^{(-t)}\cos(2\pi t)$$
"""

#Construcción de la función
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

"""## Más ejemplos con la función `figure()`"""

plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])

plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

"""## Histogramas `hist()`

Un histograma es un gráfico de barras sobre los datos que representa la dispersión de los mismos. Entonces en el podemos ver la dispersión o frecuencia con que se encuentran los datos con respecto al eje X.
"""

#Como ejemplo vamos a crear un histograma de unos datos con distribución normal
# con media 10 y varianza 5

mu, sigma = 10, 5 #media y varianza
x = mu + sigma * np.random.randn(10000) #variable aleatoria normal

n, bins, patches = plt.hist(x, 10, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probabilidad')
plt.title(r'$\sigma=5$ Histograma')
plt.text(20, .06, r'$\mu=10,\ \sigma=5$')
plt.axis([-10,30, 0, 0.085])
plt.xlabel('Datos', fontsize=14, color='blue')
plt.grid(True)
plt.show()

"""## Comentario en el gráfico

Para hacer anotaciones usamos la función `annotate()` en la cual se pasa como parámetros el texto, los valores de inicio y fin para la flecha y el punto donde se especifica donde se coloca dicho texto.
"""

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)

plt.plot(t, s, lw=2)
plt.annotate('máx local', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='green', shrink=0.05))
plt.ylim(-2, 2)
plt.show()

"""## Escala Logística"""

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

#Semilla para generar número aleatorios
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

"""# SEABORN

Para mapas de calor.
"""

import numpy as np
import seaborn as sns

np.random.seed(0) #semilla

sns.set()

#La función random.rand(d0,d1,d2,...) da un array de números aleatorios uniformes en [0,1) 
data_uniforme = np.random.rand(10, 12) #como se le dan dos valores es una matriz de datos

ax = sns.heatmap(uniform_data) #Crea el mapa de calor con los datos uniformes

# Para el sguiente gráfico vamos a variar los parámetros vmin y vmax
# estos valores son para fijar el mapa de colores, en caso contrario se infiere de los datos
# y otros argumentos de palabras claves.
ax = sns.heatmap(data_uniforme, vmin=0, vmax=1)

datos_normales = np.random.randn(10, 12) #datos aleatorios con distribución normal
#El parámetro center es el centro del mapa de colores cuando se tienen datos divergentes.
ax = sns.heatmap(datos_normales, center=0)

flights = sns.load_dataset("flights") #Cargar datos de un repositorio online
# estos datos contine tres columnas o variables, year month y passengers.
flights.head()

flights = flights.pivot("month", "year", "passengers")

ax = sns.heatmap(flights)

ax = sns.heatmap(flights, annot=True, fmt="d")
# annot si es verdadero se muestra el valor en cada celda.

ax = sns.heatmap(flights, linewidths=.5)
#linewidths agrega una línea con el grosor que se le específique entre las celdas.

ax = sns.heatmap(flights, cmap="YlGnBu")
#cmap valores del espacio de colores

ax = sns.heatmap(flights, center=flights.loc["January", 1955])
# cuando se especifica el centro del mapa de colores.

data = np.random.randn(50, 20)
ax = sns.heatmap(data, xticklabels=2, yticklabels=False)
#Los valores que corresponden a los ejes, el 2 en x significa que va colocar los valores
#cada dos dígitos.

ax = sns.heatmap(flights, cbar=False)
#cbar como False no muestra la barra de colores a la derecha

grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(flights, ax=ax,
                 cbar_ax=cbar_ax,
                 cbar_kws={"orientation": "horizontal"})

#gráficar una parte de la matriz
corr = np.corrcoef(np.random.randn(10, 200))
mask = np.zeros_like(corr) #Retorna un array de ceros con la misma dimension de lo que se le apsa.
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr, mask=mask, vmax=.3, square=True)