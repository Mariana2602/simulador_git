import os
from archivo import Archivo
from commit import Commit
from rama import Rama
from repositorio import Repositorio

class Main:
    def __init__(self):
        self.repo = Repositorio("Mi repositorio")
        self.archivos = {}
        self.init_git()
        self.iniciarConsola()

    # Crear la carpeta .git y subcarpetas para guardar la informacion enviada
    def init_git(self):
        if not os.path.exists('.git'):
            os.makedirs('.git')
            os.makedirs('.git/objects')  
            os.makedirs('.git/refs')     
            os.makedirs('.git/refs/heads')
            print("Directorio .git creado.")

    #Escribe informacion rn el archivo log para registrar las operaciones realizadas 
    def guardarComando(self, comando, resultado):
        with open('.git/log', 'a') as archivo_log:
            archivo_log.write(f"{comando} - {resultado}\n")

    #Ciclo que permite la entrada de comandos para la ejecucion del simulador
    def iniciarConsola(self):
        print("Simulador Git iniciado. Escriba 'exit' para salir.")
        while True:
            comando = input(">> ").strip()
            if comando == "exit":
                break
            elif comando.startswith("git add"):
                self.gitAdd(comando)
            elif comando.startswith("git commit"):
                self.gitCommit(comando)
            elif comando.startswith("git branch"):
                self.gitBranch(comando)
            elif comando.startswith("git checkout"):
                self.gitCheckout(comando)
            elif comando.startswith("git log"):
                self.gitLog()
            else:
                print("Comando no reconocido.")

    #Metodo que selecciona el archivo escrito y lo carga para poder modificarlo
    def gitAdd(self, comando):
        n = comando.split()
        if len(n) == 3:
            nombre = n[2]
            if nombre not in self.archivos:
                archivo = Archivo(nombre)
                self.archivos[nombre] = archivo
                mensaje = f"Archivo '{nombre}' agregado."
                print(mensaje)
            else:
                mensaje = f"Archivo '{nombre}' ya está agregado."
                print(mensaje)
        else:
            mensaje = "Comando no reconocido."
            print(mensaje)

    #Metodo que guarda el mensaje de los cambios hechos al archivo seleccionado
    def gitCommit(self, comando):
        n = comando.split(maxsplit=3)
        if len(n) == 4:
            mensaje = n[3]
            archivosModificados = list(self.archivos.values())
            if archivosModificados:
                self.repo.commitRama(mensaje, archivosModificados, "Admin")
                mensaje = f"Commit realizado con mensaje: '{mensaje}'"
                print(mensaje)
                self.archivos.clear()
            else:
                mensaje = "No hay archivos para hacer commit."
                print(mensaje)
        else:
            mensaje = "Comando no conocido"
            print(mensaje)

    #Metodo que crea ramas con el nombre escogido 
    def gitBranch(self, comando):
        n = comando.split()
        if len(n) == 3:
            nombre = n[2]
            self.repo.crearRama(nombre)
            mensaje = f"Rama '{nombre}' creada."
            print(mensaje)
        else:
            mensaje = "Comando no conocido"
            print(mensaje)
        self.guardarComando(comando, mensaje)

    #Metodo que cambia la rama de trabajo para trabajar en otra
    def gitCheckout(self, comando):
        partes = comando.split()
        if len(partes) == 3:
            nombre_rama = partes[2]
            self.repo.cambiarRama(nombre_rama)
            mensaje = f"Rama seleccionada: '{nombre_rama}'."
            print(mensaje)
        else:
            mensaje = "Comando no conocido."
            print(mensaje)
        self.guardarComando(comando, mensaje)

    #Metodo que muestra todos los commits realizados
    def gitLog(self):
        try:
            historial = self.repo.historialCommits()
            if historial:
                print("Historial de commits:")
                for commit in historial:
                    print(commit)
                    print("="*20)
            else:
                print("No hay commits en el historial.")
        except FileNotFoundError:
            print("No hay historial de commits.")
    
if __name__ == "__main__":
    Main()
