"""Crear aviso de advertencia antes de abrir la app Server App"""
'''
Datos:
    Nombre: Server App for Windows
    Lenguaje: Python
    Idioma: es-es
    Versión: 1.0 - Beta 1
    Dependencias: PySide6, os, sys, path
    Usado para: Control de servidores de minecraft bedrock en un solo lugar
'''
# (Inicio del código...)
import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget
from PySide6.QtGui import QIcon

class AlertWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.get_material_you_style())  # Aplicar el estilo Material You
        self.show_alert()

    def show_alert(self):
        # Crear un cuadro de mensaje de advertencia
        alert_box = QMessageBox(self)
        alert_box.setIcon(QMessageBox.Warning)  # Icono de advertencia
        alert_box.setWindowTitle("Alerta")      # Título de la ventana

        # Establecer el ícono de la aplicación
        app_icon = QIcon("icons/applogo.png")  # Ruta al ícono
        alert_box.setWindowIcon(app_icon)       # Asignar el ícono a la ventana

        # Mensaje detallado
        alert_message = (
            "Alerta:\n\n"
            "Esta es una versión nueva de servidor. Un nuevo programa creado NO es una herramienta de uso.\n\n"
            "Esta App se encuentra en pleno desarrollo. Por favor, reporta cualquier inconveniente.\n\n"
            "Nombre:\n"
            "Server App for Windows v1.0 - Beta 1"
        )
        alert_box.setText(alert_message)  # Mensaje completo

        # Botones personalizados
        yes_button = alert_box.addButton("Sí, deseo ejecutar", QMessageBox.YesRole)  # Botón "Sí"
        no_button = alert_box.addButton("No, prefiero salir", QMessageBox.NoRole)   # Botón "No"

        # Aplicar estilo a los botones
        yes_button.setStyleSheet("""
            QPushButton {
                background-color: #7AB2D3;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4A628A;
            }
        """)
        no_button.setStyleSheet("""
            QPushButton {
                background-color: #B9E5E8;
                color: #4A628A;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #DFF2EB;
            }
        """)

        # Mostrar el cuadro de mensaje
        alert_box.exec()

        # Verificar qué botón se presionó
        if alert_box.clickedButton() == yes_button:
            print("Ejecutando AppStartup.py...")
            self.run_app_startup()  # Ejecutar el archivo AppStartup.py
            sys.exit()  # Cerrar el script principal después de lanzar AppStartup.py
        elif alert_box.clickedButton() == no_button:
            print("Saliendo del programa...")
            sys.exit()  # Salir del programa

    def run_app_startup(self):
        """Función para ejecutar el archivo AppStartup.py en segundo plano"""
        try:
            # Usar Popen para ejecutar el archivo en segundo plano
            subprocess.Popen([sys.executable, "AppStartup.py"])
            print("AppStartup.py se ha lanzado correctamente.")
        except FileNotFoundError:
            print("Error: No se encontró el archivo AppStartup.py")
        except Exception as e:
            print(f"Error al ejecutar AppStartup.py: {e}")

    def get_material_you_style(self):
        """Define el estilo Material You con la paleta de colores proporcionada"""
        return """
            QWidget {
                background-color: #DFF2EB;
                color: #4A628A;
                font-family: "Segoe UI", sans-serif;
                font-size: 14px;
            }
            QMessageBox {
                background-color: #DFF2EB;
                border: 2px solid #B9E5E8;
                border-radius: 10px;
            }
            QMessageBox QLabel {
                color: #4A628A;
                font-size: 16px;
            }
            QPushButton {
                background-color: #7AB2D3;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4A628A;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AlertWindow()
    sys.exit(app.exec())
# (Final del código)