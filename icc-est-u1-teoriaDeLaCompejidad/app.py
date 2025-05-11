from benchmarking import Benchmarking
from sort_methods import SortMethods
import matplotlib.pyplot as plt

class App:
    if __name__ == "__main__":
        resultados = []
        tamanios = [5_000, 10_000, 30_000, 50_000, 100_000]

        benchM = Benchmarking()
        metodoOr = SortMethods()

        array_100k = benchM.build_arreglo_100_000()
        array_50k  = benchM.build_arreglo_peque(50_000, array_100k)
        array_30k  = benchM.build_arreglo_peque(30_000, array_100k)
        array_10k  = benchM.build_arreglo_peque(10_000, array_100k)
        array_5k   = benchM.build_arreglo_peque(5_000, array_100k)

        metodos = {
            "burbuja": metodoOr.ordenarBurbuja,
            "burbuja_mejorado": metodoOr.ordenarBurbujaMejorado,
            "seleccion": metodoOr.ordenarSeleccion,
            "insercion": metodoOr.ordenarInsercion,
            "shell": metodoOr.odenarShellShort, 
        }

        for tam in tamanios:
            array_peque = array_100k if tam == 100_000 else benchM.build_arreglo_peque(tam, array_100k)

            for nombre, metodo in metodos.items():
                tiempo = benchM.medir_tiempo(metodo, array_peque)
                resultados.append((tam, nombre, tiempo))

        for tam, nombre, tiempo in resultados:
            print(f"Tamaño: {tam}, Nombre: {nombre}, Tiempo: {tiempo:.6f} segundos")

        # ------------ Graficar resultados

        tiempos_by_metodo = {nombre: [] for nombre in metodos}

        for tam, nombre, tiempo in resultados:
            tiempos_by_metodo[nombre].append(tiempo)

        fig = plt.figure(figsize=(10, 6))
        for nombre, tiempo in tiempos_by_metodo.items():
            plt.plot(tamanios, tiempo, label=nombre, marker='o')

        plt.title("Comparativa de métodos\nBrandon Rivera y Erick Yunga")
        plt.xlabel("Tamaño del arreglo")
        plt.ylabel("Tiempo de ejecución (s)")
        fig.canvas.manager.set_window_title("Teoria de Complejidad")
        plt.grid()
        plt.legend()
        plt.xticks(tamanios, rotation=45) 
        plt.show()