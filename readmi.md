# Estructuras de Datos en Python

Proyecto desarrollado para la actividad **GA1-220501093-04-AA1-EV03** del programa ADSO - SENA, correspondiente al curso "Estructuras de Datos en Python".

## Descripción del proyecto

Este repositorio contiene el desarrollo práctico de los 5 módulos del recurso educativo digital de Estructuras de Datos en Python, replicando los ejemplos vistos en cada módulo y resolviendo los retos propuestos por el material formativo.

## Temas aprendidos

- **Módulo 1 - Listas**: creación y acceso, slicing, métodos para añadir (append, insert, extend) y eliminar (remove, pop, clear), ordenamiento (sort, sorted, reverse), recorrido (for, enumerate, zip, comprensiones) y copias (copy, deepcopy).
- **Módulo 2 - Tuplas**: inmutabilidad, hashabilidad y rendimiento, creación, acceso a elementos, desempaquetado básico y avanzado (operador `*`, `_`, retorno múltiple).
- **Módulo 3 - Diccionarios**: estructura clave-valor, creación, operaciones CRUD (update, pop, popitem, setdefault, fromkeys), iteración (keys, values, items) y comprensiones de diccionario.
- **Módulo 4 - Conjuntos**: elementos únicos, operaciones básicas, métodos de teoría de conjuntos (intersection, union, difference) y operadores matemáticos (`| & - ^`).
- **Módulo 5 - Comprehensions**: list, dict y set comprehensions, aplicación combinada en un caso real, y cuándo usar generadores en vez de comprehensions.

## Estructura del proyecto

python_estructuras_de_datos/
│── modulo1_listas/
│ └── reto_inventario.py
│── modulo2_tuplas/
│ └── reto_tuplas.py
│── modulo3_diccionarios/
│ └── reto_diccionario.py
│── modulo4_conjuntos/
│ └── reto_tiendas.py
│── modulo5_comprehensions/
│ └── reto_ventas.py
│── images/
│── README.md

## Evidencia de retos resueltos

### Módulo 1 - Reto: Gestión de Inventario

Sistema de inventario con listas anidadas `[nombre, cantidad, precio]`.

![Reto Inventario](images/Captura%20de%20pantalla%202026-08-01%20114838.png)

### Módulo 2 - Reto: Sistema de Películas

Catálogo de películas con tuplas, desempaquetado y búsqueda por director.

![Reto Tuplas](images/captura%20de%20pantalla%202.png)

### Módulo 3 - Reto: Análisis de Ventas por Región

Análisis de un diccionario anidado con totales, máximos y reportes por porcentaje.

![Reto Diccionarios](images/Captura%20de%20pantalla3%202026-08-01%20115750.png)

### Módulo 4 - Reto: Tiendas y Recomendaciones de Películas

Operaciones de conjuntos sobre catálogos de tiendas y géneros de usuarios.

![Reto Conjuntos](images/Captura%20de%20pantalla4%202026-08-01%20120051.png)

### Módulo 5 - Reto: Analizador de Ventas con Comprehensions

Análisis de ventas combinando list, dict y set comprehensions.

![Reto Comprehensions](images/Captura%20de%20pantalla5%202026-08-01%20120222.png)

## Reflexión personal

Trabajar con estructuras de datos en Python me ayudó a entender que elegir la estructura correcta es tan importante como escribir el código mismo. Antes usaba listas para casi todo, pero ahora entiendo cuándo tiene más sentido una tupla (por ejemplo, para datos que no deben cambiar, como coordenadas), un diccionario (cuando necesito relacionar una clave con un valor, como en el análisis de ventas por región), o un conjunto (cuando la unicidad de los elementos es la prioridad, como en la comparación de catálogos entre tiendas).

El módulo de tuplas me hizo notar detalles que antes pasaba por alto, como la diferencia entre `(42)` y `(42,)`, o que una tupla puede usarse como clave de un diccionario justamente por ser inmutable. En diccionarios, el reto de ventas por región fue el que más me costó al principio, porque tuve que pensar en iteraciones anidadas y en cómo acumular valores sin perder la relación entre región y trimestre. Con conjuntos, entendí el valor real de operaciones como la intersección o la diferencia simétrica, aplicadas a un caso tan cotidiano como comparar catálogos de tiendas o gustos de usuarios.

Las comprehensions fueron el cierre perfecto: ver cómo un bucle de varias líneas se puede resumir en una sola, sin perder claridad, cambió la forma en que ahora escribo código en Python. El reto final, que combinó las tres comprehensions sobre un mismo dataset de ventas, me sirvió para conectar todo lo aprendido en los módulos anteriores.

En general, este proyecto me dejó más seguro trabajando con datos en Python y más consciente de que cada estructura tiene un propósito específico — no se trata de memorizar sintaxis, sino de saber cuándo usar cada una según el problema que se quiere resolver.

## Autor

Santiago Varela Peña - Aprendiz ADSO, SENA
