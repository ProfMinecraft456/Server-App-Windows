# Server App For Windows

**Server App For Windows** es una aplicación desarrollada en Python para gestionar servidores de Minecraft Bedrock utilizando el archivo `bedrock_server.exe`. Esta aplicación está diseñada para funcionar en dispositivos Windows con especificaciones modestas, por lo que no necesitas una computadora de alto rendimiento. Aunque puede haber algunas pérdidas de rendimiento, la aplicación está optimizada para ofrecer una experiencia aceptable en cualquier equipo. Esta es la versión beta inicial (1.0 - Beta 1) del proyecto **Minecraft Server for Windows**.

---

## Requisitos de Instalación (Incluyendo el Servidor Dedicado)

- **Procesador:** Intel® Core i3-2120 o AMD® Ryzen 3 3200.
- **RAM:** 2 GB o superior.
- **Almacenamiento:** 1-2 GB para packs, shaders y mods (se recomienda SSD).
- **Sistema Operativo:** Windows 10 (versión 1703) o Windows Server 2016.
- **Conexión de Red:** Estable con al menos 10 Mbps para una experiencia fluida.
- **Privilegios Administrativos:** No requeridos para la instalación.

---

## Instalación

1. Descarga el instalador **ServerAppInstallerBeta1.exe** desde el siguiente enlace: [Server App Installer](https://drive.google.com/file/d/1qc438yzKh3Ga4CFQ-5vlJmJyyhvAzFi8/view?usp=sharing).
2. Abre el archivo descargado (no requiere privilegios administrativos).
3. Haz clic en el botón "Examinar" y selecciona una carpeta para instalar la aplicación.
4. Pulsa el botón "Extraer" y espera a que finalice el proceso.
5. Dirígete al directorio donde se instaló la aplicación.
6. Abre una ventana de comandos (CMD) en ese directorio y ejecuta el siguiente comando:
   ```bash
   NodeRunner.cmd -App
   ```
   Esto verificará que todos los archivos necesarios estén presentes y abrirá la aplicación.
7. Selecciona el directorio donde se encuentra el archivo `bedrock_server.exe` para ejecutar el servidor dedicado.

---

## Uso

La aplicación se organiza en dos pestañas principales: **Inicio** y **Archivos**.

### Pestaña Inicio
- **Controles**:
  - **INICIAR**: Inicia el servidor Bedrock.
  - **DETENER**: Detiene el servidor.
  - **REINICIAR**: Detiene y reinicia el servidor.
- **Información del Servidor**:
  - **IP del Servidor:** Obtiene la IP local para acceder.
  - **Puerto:** Establecido en el archivo `server.properties`.
  - **Versión:** Muestra la versión del servidor basada en `bedrock_server.exe`.
- **Rendimiento**:
  - **Uso de CPU:** Indica el consumo del proceso `bedrock_server.exe` (puede no ser preciso).
  - **Uso de RAM:** Muestra el uso de memoria (con precisión aceptable).
  - **Uso de Red:** Monitorea el tráfico de red (puede mostrar valores inexactos).

### Comandos de NodeRunner
- `NodeRunner.cmd -App`: Inicia la aplicación normalmente.
- `NodeRunner.cmd -AppRes`: Restaura los valores predeterminados de la aplicación.

---

## Funcionamiento

1. Al iniciar por primera vez, la aplicación solicitará el directorio donde se encuentra el archivo `bedrock_server.exe`.
2. Ejecutará el servidor para que Python pueda leer los datos necesarios.
3. Obtendrá la IP local de la red.
4. Permite renombrar, borrar y crear archivos.
5. Puede abrir/editar archivos de los siguientes formatos:
   - `.properties`, `.json`, `.txt`, `.exe`, `.zip`, `.tar.gz`.

---

## Estructura de Directorios

- **releases**: Carpeta que contiene los instaladores de las versiones de la aplicación.
- **1.0 - Beta 1**: Contiene los archivos y dependencias de la versión Beta 1, incluyendo:
  - **Code**: Código fuente en Python (sin empaquetar).
  - **exe-code**: Código empaquetado como ejecutable `.exe` (no incluido en el instalador).

---

## Contribución

Puedes contribuir al proyecto mediante las siguientes opciones:
- Modificar el código y enviarlo a mi [correo de contacto](mailto:profmcyt@hotmail.com): `profmcyt@hotmail.com`.
- Enviar sugerencias o comentarios para mejorar futuras versiones.

---

## Librerías Utilizadas

A continuación, se listan las librerías necesarias para ejecutar la aplicación:

- **PySide6**  
- **Rich**  
- **Subprocess**  
- **psutil**  
- **JSON**  
- **OS**  
- **pygame**  
- **shutil**  
- **time**  

Para instalarlas, ejecuta los siguientes comandos en tu terminal:
```bash
pip install PySide6
pip install pygame
pip install rich
pip install psutil
```

---

¡Gracias por usar **Server App For Windows**!
