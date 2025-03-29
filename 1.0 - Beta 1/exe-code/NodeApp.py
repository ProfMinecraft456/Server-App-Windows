import os
import time
import sys
from rich.progress import Progress
from rich.console import Console

app = "ServerAppBeta1Warn.exe"

# Lista de archivos y directorios a verificar
files_to_check = [
    "AppReset.exe", "AppStartup.exe", "ServerAppBeta1Warn.exe",  "icons/app.png",
    "icons/applogo.png", "icons/back.png", "icons/cpu.png", "icons/delete.png",
    "icons/edition.png",  "icons/file.png", "icons/fileexplorer.png",  "icons/folder.png",
    "icons/home.png", "icons/ip.png",  "icons/jsonfile.png", "icons/letsgo.png",
    "icons/network.png", "icons/newfile.png", "icons/newfolder.png", "icons/next.png",
    "icons/performance.png", "icons/port.png", "icons/prop.png", "icons/ram.png",
    "icons/rename.png", "icons/restart.png", "icons/save.png", "icons/server.png", 
    "icons/start.png", "icons/stop.png", "icons/txtfile.png", "icons/version.png",
    "icons/zipfile.png", "settings/serverappsetting.json", "sounds/startup.wav", "styles/styles.css"
]

# Función para verificar la existencia de los archivos
def check_files(files):
    missing_files = []
    with Progress() as progress:
        task = progress.add_task("[cyan]Verificando archivos...\r", total=len(files))
        for file in files:
            time.sleep(0.25)  # Retardo de 1 segundo entre cada verificación
            if not os.path.exists(file):
                missing_files.append(file)
            progress.update(task, advance=1)
    return missing_files

# Función principal
def main():
    console = Console()
    missing_files = check_files(files_to_check)

    if missing_files:
        console.print("[bold red]Faltan los siguientes componentes:[/bold red]")
        for file in missing_files:
            console.print(f"- {file}")
        console.print("[bold red]La aplicación no puede continuar. Saliendo...[/bold red]")
    else:
        console.print("[bold green]Todos los componentes están presentes.[/bold green]")
        console.print(f"[bold green]Ejecutando {app}...[/bold green]")
        console.print(f"[bold green]Preparando Inicio de app...[/bold green]")
        os.system(f"{app}")
        console.print("[bold green]Script ejecutado.[/bold green]")
        sys.exit(0)  # Cierra Python definitivamente

if __name__ == "__main__":
    main()