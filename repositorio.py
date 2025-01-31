#Clase que administra toda la informacion que estan en las ramas y los commits
from rama import Rama
from commit import Commit

class Repositorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ramas = {}
        self.ramaEscogida = None
        self.crearRama("main")

    #Metodo para crear nueva rama
    def crearRama(self, nombre):
        ramaNueva = Rama(nombre)
        self.ramas[nombre] = ramaNueva
        if not self.ramaEscogida:
            self.ramaEscogida = ramaNueva

    #Metodo para cambiar la rama actual por otra rama 
    def cambiarRama(self, nombre):
        if nombre in self.ramas:
            self.ramaEscogida = self.ramas[nombre]
        else:
            print(f"La rama '{nombre}' no existe.")

    #Metodo que establece un id e instancia en el objeto commiNuevo la clase Commit, para agregarlos a la rama
    def commitRama(self, mensaje, archivos, autor):
        if self.ramaEscogida:
            idCommit = len(self.ramaEscogida.commits) + 1
            commitNuevo = Commit(idCommit, mensaje, archivos, autor)
            self.ramaEscogida.agregar(commitNuevo)
        else:
            print("No existe la rama.")

    #metodo que extrae toda la informacion de forma ordenada de los commits realizados para guardarlos en un vector
    def historialCommits(self):
        historial = []
        for rama in self.ramas.values():
            historial.extend(rama.commits)
        historial.sort(key=lambda commit: commit.fecha, reverse=True)
        return historial

    def __str__(self):
        ramas = ", ".join(self.ramas.keys())
        return (f'Repositorio: {self.nombre}\n'
                f'Ramas: {ramas}\n'
                f'Rama actual: {self.ramaEscogida.nombre if self.ramaEscogida else "Ninguna"}')
