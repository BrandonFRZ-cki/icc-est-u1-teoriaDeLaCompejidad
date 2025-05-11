 # INFROME DE README

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

 - La comparación de los métodos de ordenamiento muestra que, en términos de notación Big-O, los algoritmos como BURBUJA tienen un mejor rendimiento promedio con \( O(n \log n) \), mientras que otros como BubbleSort tienen un peor rendimiento con \( O(n^2) \). Por lo tanto, BURBUJA es más rápido en la mayoría de los casos, especialmente para conjuntos de datos grandes. (**EJEMPLO INFORMACION INCORRECTA**) 