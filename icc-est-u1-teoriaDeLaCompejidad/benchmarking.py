import random
import time
class Benchmarking:
    
    def __init__(self): # Constructor
        print("Inicializado El Bench")
    
    def build_arreglo_100_000(self):
        gran_array=[]
        for i in range(100_000):
            numero = random.randint(0,99999)
            gran_array.append(numero)
        return gran_array
    
    def build_arreglo_peque(self,tam,arreglo):
        gran_array = arreglo.copy()
        arr_peque = []
        for i in range(tam):
            arr_peque.append(gran_array[i])
        return arr_peque
    
    def medir_tiempo(self,tarea,array):
        inicio = time.perf_counter()
        tarea(array)
        fin = time.perf_counter()
        return fin-inicio
    


