# Server App For Windows:
El proyecto "Server App For Windows", es una aplicación diseñada en Python para la dedicación del control de serviodres de Minecraft Bedrock junto con el archivo `bedrock_server.exe`. Esta aplicación esta dedicada a dispositivos windows con especificaciones MODESTAS, por lo que quiere decir que no requieres de una PC monstruo para esta aplicación ya que esta optimizada para cualquier dispositivo, si con algunas pérdidas de rendimiento comprendibles. En esta version fase beta (la 1.0 - Beta 1) se empezara el proyecto minecraft server for windows.
## Requisitos de instalación (Incluyendo el servidor dedicado):
- **Procesador:** Intel® Core i3-2120 o bien AMD® Ryzen 3 3200.
- **RAM:** 2GB o superior.
- **Almacenamiento:** 1GB - 2GB para packs, shaders y mods, (SSD Recomendado).
- **OS:** Windows 10 1703 o bien Windows Server 2016.
- **Red:** Conectividad estable de 10Mbps para una experiencia sin complicaciones.
- No se requiere privilegios administrativos para la instalación.
## Instalacíon:
- Descarga el archivo ServerAppInstallerBeta1.exe de este link: [Server App Installer](https://drive.google.com/file/d/1qc438yzKh3Ga4CFQ-5vlJmJyyhvAzFi8/view?usp=sharing).
- Una vez descargado el archivo lo abres (No requiere privilegios administrativos).
- Luego pulsas el boton "Examinar" (Recuerda que debes tener una carpeta para esta app).
- Pulsas el boton "Extraer" y esperas un momento.
- Luego ve al directorio donde se instalo la app.
- Luegos abres cmd para el directorio de esa app y escribes este comando: `NodeRunner.cmd -App` esto verificara si todos los archivos existen y luego abre la app.
- Seleccionas el directorio donde esta el archivo `bedrock_server.exe` para la ejecucción (Servidor dedicado por separado).
## Uso:
- El Programa mostrara todo en dos pestañas (Inicio y Archivos).
- En la de inicio encuentras:
    - **El Inicio:**
        - **3 botones:** [INICIAR], [DETENER], [REINICIAR]:
            - **Iniciar:** Inicia el servidor bedrock
            - **Detener:** Detiene el servidor
            - **Reiniciar:** Detiene el servidor y lo vuelve a iniciar
        - **IP del Servidor** para acceder (Uso de tu IP local)
        - **Puerto:** Establecido por el archivo `server.properties`
        - **Versión:** Versión del servidor con `bedrock_server.exe`
    - **Rendimiento:**
        - **Uso de CPU:** Uso de la cpu del proceso `bedrock_server.exe` **(ADVERTENCIA NO ES PRECISO CON EL USO ASI QUE PUEDE VARIAR)**
        - **Uso de RAM:** Uso de la ram del proceso incluyendo la app **Tiene Precisión ACEPTABLE**
        - **Uso de red:** Uso de red del proceso **NO ES PRECISO COMO EL DE LA CPU ASI QUE TENDRIA UN USO DE HASTA 12344543MB/s FALSOS**
- **Comandos del NodeRunner:** Los comandos admitidos son:
    - `NodeRunner.cmd -App`: Este comando inicia la app con normalidad
    - `NodeRunner.cmd -AppRes`: Este comando inicia el modo restauración de valores de la app (Empezar desde cero)
## Funcionamiento:
- La app por primera vez te va a pedir el directorio donde esta el archivo `bedrock_server.exe`
- Esta ejecutará para que el python lea los datos
- La IP es obtenida de la red local
- Permite renombrar, borrar, crear todo tipo de archivo
- Puede abrir/editar archivos .properties, `.json`, `.txt`, `.exe`, `.zip`, `.tar.gz`
## Directorios:
- releases: carpeta donde están ubicados los lanzamientos del las versiones de la app. En esta carpeta esta ubicado el instalador de cada versión.
- 1.0 - Beta 1: carpeta donde estan todos los archivos y dependencias del la version 1 Beta 1 de la app. Dentro esta la carpeta "Code" el cual esta el codigo python sin ejecutable y la "exe-code" donde estan los codigos pero ejecutar como ejecutable exe que no viene incluido.
## Contribución:
- Puede contribuir modificando codigo y enviando a mi [correo de contacto](mailto:profmcyt@hotmail.com) (profmcyt@hotmail.com) o enviar comentarios para mejoras para la siguiente versión
## Librerías
- PySide6
- Rich
- Subprocess
- psutil
- JSON
- OS
- pygame
- shutil
- time

```Bash
pip install PySide6
pip install pygame
pip install shutil
pip install rich