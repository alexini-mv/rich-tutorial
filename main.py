import time

from rich import print
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install
install()

# 1.- Print Statemetn
print(" 1.- Función Print ".center(60, "="))
print({"uno": [1, 2, 3], "dos": {"tres": True}}, "")


# 2.- Console Object
print(" 2.- Objeto Console ".center(60, "="))
console = Console()

console.print("Hola mundo")
console.print("Hola mundo", style="bold")
console.print("Hola mundo", style="bold green")
console.print("Hola mundo", style="bold green underline on red")

console.print(
    "[bold green]Saludos[/bold green] [bold red]Terricolas[/bold red] [blink]:boom:[/blink]\n")

# 3.- Text Object
print(" 3.- Objeto Text ".center(60, "="))

text = Text("¡Los marcianos llegaron ya a la Tierra!\n")
text.stylize(style="bold red", start=5, end=14)
text.stylize(style="bold cyan", start=32, end=38)

console.print(text)

# 4.- Custom Theme
console.print(" 4.- Tema Personalizado ".center(60, "="))

tema_personalizado = Theme({"exito": "italic green",
                            "error": "bold red",
                            "precaucion": "yellow blink"})

console = Console(theme=tema_personalizado, record=True)

console.print("Descarga completa", style="exito")
console.print("Actualización requerida", style="precaucion")
console.print("Recurso no encontrado", style="error")

console.print("Este mensaje [precaucion]parpadeará[/] todo el tiempo.\n")

# 5.- Emojis
console.print(" 5.- Emojis ".center(60, "="))

console.print(":thumbs_up: ¡Descargado!")
console.print(":apple: :bug: 🥳 🤠 😍 🥰 😘 🫣 \n")

# 6.- Logs
console.print(" 6.- Logs ".center(60, "="))

for i in range(10):
    console.log(f"El proceso {i} inicializó.")
    time.sleep(0.25)
print("")
time.sleep(1)

# 7.- Traceback
console.print(" 7.- Traceback ".center(60, "="))

def suma(a, b):
    console.log("Realizamos una suma:", log_locals=True)
    return a + b

try:
    suma(1, 2)
    suma(5, 9)
    suma(7, "tres")
except TypeError:
    console.print_exception()

print("")

# 8.- Exportar la salida
console.print(" 8.- Exportar la salida ".center(60, "="))

console.log("Guardando todos los output en output.html")
console.save_html("output.html")