from benchmarking import Benchmarking
#from sort_methods import SortMethods

class App:
    if __name__ == "__main__":
        resultados = []
        tamanios = [5_000 , 10_000 , 30_000 , 50_000,]

        for tam in tamanios:
            benchM = Benchmarking()
            #metodoOr = SortMethods()
            
            # --------- Creo los arreglos
            array_100k = benchM.build_arreglo_100_000()
            array_50k  = benchM.build_arreglo_peque(50_000,array_100k)
            array_30k  = benchM.build_arreglo_peque(30_000,array_100k)
            array_10k  = benchM.build_arreglo_peque(10_000,array_100k)
            array_5k   = benchM.build_arreglo_peque(5_000,array_100k)
            #
            


