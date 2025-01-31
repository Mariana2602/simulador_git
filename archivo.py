#En esta clase se ejecuta el constructor llamando al metodo leer para guardar el contenido del archivo
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.informacion = self.leer()

    def leer(self):
        try:
            with open(self.nombre, 'r') as archivo:
                return archivo.read()
        except FileNotFoundError:
            return "El archivo no existe."

    def __str__(self):
        return f'Archivo: {self.nombre}, Contenido: {self.informacion[:30]}...'
    