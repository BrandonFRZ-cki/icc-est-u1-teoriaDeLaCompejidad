class SortMethods:
    def ordenarBurbuja(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def ordenarBurbujaMejorado(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        
        for i in range(n):
            intercambiado = False  
            for j in range(0, n - 1 - i):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    intercambiado = True  
            
            if intercambiado == False:  
                break
        
        return arreglo

    def ordenarSeleccion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range(n - 1):
            menor = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[menor]:  
                    menor = j
            if menor != i:
                arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]
        return arreglo

    def ordenarInsercion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)

        for i in range(1, n):  
            aux = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > aux:  
                arreglo[j + 1] = arreglo[j]  
                j -= 1
            arreglo[j + 1] = aux  
        return arreglo

    def odenarShellShort(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        gap = n // 2  

        while gap > 0:  
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]  
                    j -= gap
                arreglo[j] = temp  
            gap //= 2  
        return arreglo