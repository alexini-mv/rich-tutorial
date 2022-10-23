import time

from rich import print
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.terminal_theme import MONOKAI
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import track
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

with console.status("[bold green]Working on tasks...", spinner="arrow3") as status:
    for i in range(10):
        console.log(f"El proceso {i} inicializó.")
        time.sleep(0.75)
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
    console.print_exception(show_locals=True)

print("")

# 8.- Exportar la salida
console.print(" 8.- Exportar la salida ".center(60, "="))

console.log("Guardando todos los output en output.html \n")
console.save_html("output.html", theme=MONOKAI)

# 9.- Tablas
console.print(" 9.- Tablas ".center(60, "="))

table = Table(title="Lista de compras", title_style="bold cyan")

table.add_column("Producto", header_style="bold green", style="green")
table.add_column("Categoría", header_style="bold magenta",
                 style="magenta", justify="center")
table.add_column("Precio", header_style="bold blue",
                 style="blue", justify="right")

table.add_row("Manzanas", "Frutas", "$52.00")
table.add_row("Plátano macho frito", "Botanas", "$25.60", style="bold yellow")
table.add_row("Vino tinto del Valle de Guadalupe",
              "Vinos y Destilados", "$159.00", end_section=True)

table.add_section()

table.add_row("Galletas de chocolate", "Dulces", "$24.50")
table.add_row("Pan de muerto", "Panaderia", "$15.00")

console.print(table, "")

# 10.- Markdown
console.print(" 10.- Markdown ".center(60, "="))

texto = """
# Esto es un titulo
Aquí tenemos texto en *cursiva*, en **negritas** y en ***cursiva negritas***.

## Esto es un subtitulo

Además agregamos una lista
* Uno
* Dos
  - Lista anidada
* Tres

Agregamos otra lista
1. Uno
2. Dos
3. Tres

Así se vería un bloque de código:

```python
from rich.text import Text

text = Text("¡Los marcianos llegaron ya a la Tierra!")
text.stylize(style="bold red", start=5, end=14)
text.stylize(style="bold cyan", start=32, end=38)

console.print(text)
```
Esto es un [hipervinculo](https://www.google.com).

"""
md = Markdown(texto)
console.print(md, "")

# 11.- Barra de Progreso
console.print(" 11.- Barra de Progreso ".center(60, "="))
console.print("Ejemplo de una barra de progreso: \n")

for i in track(range(15), console=console, description="Descargando..."):
    time.sleep(0.25)
console.print("")

# 11.- Inspector de Objetos
console.print(" 11.- Inspector de Objetos ".center(60, "="))

from rich import inspect
inspect("Soy un string", methods=True)