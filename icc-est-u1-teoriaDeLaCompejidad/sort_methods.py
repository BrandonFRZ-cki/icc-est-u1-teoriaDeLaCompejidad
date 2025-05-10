class SortMethods:
    def ordenarBurbuja (self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range (n):
            for j in range(i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def ordenarBurbujaMejorado (self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range(n):
            for j in range(0,n-1-i):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo  

    def ordenarSeleccion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range (n-1):
            menor = i
            for j in range(i+1,n):
                menor = j
            if menor != i:
                arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]
        return arreglo

    def ordenarInsercion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range (n):
            aux = arreglo[i]
            j = i - 1

            while j >= 0 and arreglo[j] < aux:
                arreglo[j+1], arreglo[j]
                j -= 1
                arreglo[j+1] = aux
        return arreglo
    
    def odenarShellShort(self, arreglo):
        

            


