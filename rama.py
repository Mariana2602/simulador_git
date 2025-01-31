#Clase que almacena los commits para formar una linea de las fotografías hechas de manera ordenada
class Rama:
    def __init__(self, nombre):
        self.nombre = nombre
        self.commits = []
        self.head = None

    #Se agregan los commits al vector
    def agregar(self, commit):
        self.commits.append(commit)
        self.head = commit

    #Se ordenan los commit
    def historial(self):
        return sorted(self.commits, key=lambda commit: commit.fecha, reverse=True)

    def __str__(self):
        return (f'Rama: {self.nombre}\n'
                f'HEAD: {self.head.id_commit if self.head else "None"}\n'
                f'Commits: {[commit.id_commit for commit in self.commits]}')
