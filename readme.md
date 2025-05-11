 # INFROME README

# Práctica Teoria de la Complejidad

## 📌 Información General

- **Título:** Algoritmos de Ordenamiento
- **Asignatura:** Estructura de Datos
- **Carrera:** Computación
- **Estudiantes:** Brandon Rivera, Erick Yunga
- **Fecha:** 10/05/2025
- **Profesor:** Ing. Pablo Torres

---

## 🎯 Objetivos
- Relaciona las técnicas de ordenamiento.
- Desarrolla módulos que emplean técnicas de ordenamiento

## 🛠️ Descripción

Este proyecto implementa y compara diferentes algoritmos de ordenamiento en Python, incluyendo:
### 🗂️ Métodos de Ordenamiento : [sort_methods.py](/icc-est-u1-teoriaDeLaCompejidad/sort_methods.py/)

---
    Clase en la cual se implementan los diferentes algoritmos de ordenamiento, tales como: método de burbuja, burbuja mejorado, selección, inserción y shell. 
    En cada uno de estos métodos se procura utilizar .copy() para asegurar que el arreglo original no sea modificado y se mantenga sin ordenar.
---
### 🧮 Crear Arreglos y Medir Tiempo de Ejecucion : [benchmarking.py](/icc-est-u1-teoriaDeLaCompejidad/benchmarking.py)
---
    En la clase Benchmarking se genera el arreglo más grande, compuesto por 100 000 números aleatorios entre 0 y 99 999. Posteriormente, otro método se encarga de crear los subarreglos a partir de este arreglo principal, ya que la práctica requiere que los arreglos de menor tamaño (5 000 ; 10 000 ; 30 000; 50 000 elementos) estén contenidos dentro del arreglo más grande. Finalmente, se implementa un método para medir el tiempo de ejecución utilizando perf_counter(), ya que proporciona una medición precisa del tiempo transcurrido, sin verse afectada por factores externos al programa.
---
### 📈 Ejecución del programa y Creación de Gráfica : [app.py](/icc-est-u1-teoriaDeLaCompejidad/app.py)
---
    Para ejecutar el programa, en la clase App se instancian las clases SortMethods y Benchmarking. Inicialmente, se generan los arreglos con tamaños de 5,000; 10,000; 30,000; 50,000 y 100,000 elementos. Luego, se crea un diccionario que contiene los métodos de ordenamiento: burbuja, burbuja mejorado, selección, inserción y shell. Finalmente, se utiliza la biblioteca matplotlib.pyplot para generar una gráfica que representa visualmente la relación entre el tamaño del arreglo y el tiempo de ejecución de cada algoritmo.
---
## ✍🏻 Resultados 
### Resultado Obtenido en Consola:
![ResultadosConsola](/icc-est-u1-teoriaDeLaCompejidad/img/comparativa_de_metodos.png)
### Gráfica 
![Gráfica](/icc-est-u1-teoriaDeLaCompejidad/img/grafico_comparativa_de_metodos.png)
### Tabla de resultados
| Metodo de Ordenamiento | 5k      | 10k     |30k       | 50k       |     100k  |
| ---                    | ---     | ---     | ---      | ---       | ---       |
| `burbuja`              | 0.666 s | 2.837 s | 24.453 s | 73.085 s  | 317.4 s   |
| `burbuja_mejorado`     | 1.059 s | 4.376 s | 38.835 s | 124.036 s | 521.953 s |
| `seleccion`            | 0.466 s | 1.842 s | 19.786 s | 53.327 s  | 201.117 s |
| `insercion`            | 0.468 s | 2.031 s | 20.204 s | 59.029 s  | 227.839 s |
| `shell`                | 0.010 s | 0.023 s | 0.1357 s | 0.402 s   | 0.416 s   |
### Analisis de resultado

##  CONCLUCIONES CON TERMINOLOGIA DE NOTACION 

# 🔍 Análisis y Conclusiones
---
## Conclusiones Brandon Rivera:

Los resultados muestran cómo la **complejidad de los algoritmos** impacta su rendimiento al incrementar 
el tamaño del arreglo. Los métodos con **\(O(n^2)\)** se vuelven cada vez más lentos, mientras que 
**Shell Sort**, con una complejidad cercana a **\(O(n \log n)\)**, mantiene tiempos de ejecución bajos 
y estables.

- **🫧 Burbuja \(O(n^2)\)** 
  - Fue el algoritmo menos eficiente, con tiempos que aumentan drásticamente. Para **100,000 elementos**, tardó **5 minutos 17 segundos**, confirmando que no es viable para conjuntos grandes.
- **🫧 Burbuja Mejorado \(O(n^2)\)**
  - En lugar de optimizar el rendimiento, fue aún más lento. Con **100,000 elementos**, tardó **8 minutos 41 segundos**, mostrando que la optimización aplicada no tuvo impacto en este caso.
- **🤏🏻 Selección \(O(n^2)\)** 
  - Tuvo tiempos aceptables en arreglos pequeños, pero empeoró con volúmenes mayores. En **100,000 elementos**, tardó **3 minutos 21 segundos**, manteniéndose por debajo de Burbuja Mejorado pero aún poco eficiente.
- **📥 Inserción \(O(n^2)\)** 
  - Siguió un patrón similar a Selección, con tiempos similares en arreglos pequeños, pero en **100,000 elementos**, tardó **3 minutos 47 segundos**, evidenciando que no escala bien con grandes volúmenes de datos.
- **🦘Shell Sort \(O(n \log n)\)** 
  - Fue el más eficiente, con tiempos casi constantes. En **100,000 elementos**, tardó **0.41 segundos**, lo que lo convierte en la mejor opción para manejar grandes conjuntos de datos.

Este análisis confirma que **los algoritmos cuadráticos no son recomendables para grandes volúmenes de datos**, mientras que **Shell Sort es una mejor alternativa por su estructura de *gaps decrecientes***. Elegir el algoritmo adecuado puede hacer una gran diferencia en eficiencia y rendimiento.


## Conclusiones Erick Yunga:

    - Shell Sort resultó ser el más eficiente de todos los algoritmos evaluados, manteniendo tiempos de ejecución muy bajos incluso con 100,000 elementos.

    - Burbuja Mejorado, a pesar de ser una versión optimizada, no logró superar al método burbuja estándar, lo cual demuestra que la mejora aplicada no fue útil en este escenario.

    - Selección fue más eficiente que burbuja y burbuja mejorado en la mayoría de los casos, especialmente en tamaños intermedios y grandes.

    - Inserción funcionó bien con arreglos más pequeños, pero su eficiencia disminuyó al trabajar con mayores volúmenes de datos.

    - Burbuja fue el algoritmo menos eficiente, con tiempos de ejecución significativamente más altos, reafirmando su desventaja frente a métodos más avanzados.
---
