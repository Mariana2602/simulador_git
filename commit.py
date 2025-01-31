#Esta clase recibe parametros que son la informacion que se guardara para los commit
import datetime

class Commit:
    def __init__(self, idCommit, mensaje, archivosModificados, autor):
        self.idCommit = idCommit
        self.mensaje = mensaje
        self.fecha = datetime.datetime.now()
        self.archivosModificados = archivosModificados
        self.autor = autor

    #Formato de impresión 
    def __str__(self):
        archivos = ", ".join([archivo.nombre for archivo in self.archivosModificados])
        return (f'Commit ID: {self.idCommit}\n'
                f'Mensaje: {self.mensaje}\n'
                f'Fecha: {self.fecha}\n'
                f'Archivos modificados: {archivos}\n'
                f'Autor: {self.autor}')
