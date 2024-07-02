class DATA:
    def __init__(self, n_archivo, datos=None, valores=None, clases=None):
        self.n_archivo = n_archivo
        self.datos = datos if datos is not None else []
        self.valores = valores if valores is not None else []
        self.clases = clases if clases is not None else []

    def obtener_datos(self):
        try:
            with open(self.n_archivo, 'r') as archivo:
                self.datos = []
                for linea in archivo:
                    try:
                        valores_str = linea.rstrip().split(',')
                        valores_int = [int(valor) for valor in valores_str]
                        self.datos.append(valores_int)
                    except ValueError as e:
                        print(f"Error al convertir los valores a enteros: {e}")
        except FileNotFoundError as e:
            print(f"Error al abrir el archivo: {e}")
        except Exception as e:
            print(f"Un error inesperado ocurrió: {e}")

    def separar_datos(self):
        self.valores = []  
        self.clases = []   
        for arreglo in self.datos:
            self.valores.append(arreglo[:-1])  
            self.clases.append(arreglo[-1])  