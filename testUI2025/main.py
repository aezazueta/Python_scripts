import sys      #librerias del sistema  
from PyQt5 import uic
from PyQt5.QtWidgets import *

'''
    Descripción de las librerias a importar:
        *sys: es un módulo que proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y funciones que interactúan con el intérprete.
        *uic: es un módulo de PyQt5 que permite cargar archivos .ui (diseños de interfaz de usuario creados con Qt Designer) y convertirlos en clases de Python.
        *PyQt5: es un conjunto de enlaces de Python para la biblioteca Qt, que se utiliza para crear aplicaciones gráficas de usuario (GUI).
        *QtWidgets: es un módulo de PyQt5 que contiene clases para crear y gestionar widgets de la interfaz de usuario, como botones, cuadros de texto, etiquetas, etc.
'''

class MainWindow(QMainWindow):
    def __init__(self):                         #Constructor de la clase MainWindow necesaria para inicializar la ventana principal de la aplicación y atributos de la misma.
                                                # Todo lo que se necesite cargar al inicio se pone dentor de esta función.
        super(MainWindow, self).__init__()      #Llama al constructor de la clase padre (QMainWindow) y carga en memoria el archivo de diseño de la interfaz de usuario.
        uic.loadUi("MainWindow.ui", self)        #Carga el archivo de diseño de la interfaz de usuario (main.ui) y lo aplica a la instancia de la clase MainWindow.
        self.setWindowTitle("UI suma de 2 números") #Establece el título de la ventana principal de la aplicación.
        self.btn_suma.clicked.connect(self.suma_numeros)

    def suma_numeros(self):
        num1, num2 = 0,0                            # inicialización de variables
        num1 = int(self.te_valor1.toPlainText()) # Se mandan llamar a los obj input_valor1 y input_valor2 de la instancia de la ventana actual (self) y 
        num2 = int(self.te_valor2.toPlainText()) # se extraen en texto plano sus valores, luego se convierten en entero.
        self.lcd_resultado.display(num1+num2)       # se le asigna el valor de la suma mediante la función display (se usa display por ser un lcd display)

if __name__ == '__main__':
    app = QApplication(sys.argv)            #Crea una instancia de QApplication, que es necesaria para cualquier aplicación Qt. sys.argv se utiliza 
                                            #para pasar argumentos de línea de comandos a la aplicación.

    screen = MainWindow()                   #Crea una instancia de la clase MainWindow, que representa la ventana principal de la aplicación.
    screen.show()                           #Muestra la ventana principal en la pantalla.
    sys.exit(app.exec_())                   #Inicia el bucle de eventos de la aplicación y espera a que se cierre. Cuando se cierra, se sale del programa con el código de salida correspondiente.
        