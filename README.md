# Tutorial de Rich
Rich es un paquete de Python para texto enriquecido y tener un formato hermoso en la terminal. La API Rich facilita la adición de color y estilo a la salida del terminal. Rich también puede representar tablas bonitas, barras de progreso, markdown, código fuente resaltado por sintaxis, trazos y más.

Rich funciona con Jupyter notebooks sin necesidad de configuración adicional.

## Instalación
Para instalar es tan fácil como hacer:
```console
$ python -m pip install rich
```
Para probar la salida en la terminal:
```console
$ python -m rich
```

## Print
Se puede sobre escribir la función `print` para poder imprimir con toda las caracteristicas y riquezas gráficas de `Rich`. De la siguiente forma:

```python
from rich import print

print({"uno": [1,2,3], "dos": {"tres": true} })
```
## Console object
Para tener una salida más profesional, es recomendable enviar las salidas que se implimirán al objeto `rich.console.Console`. Este se usa de la siguiente forma:

```python
from rich.console import Console
console = Console()

console.print("Hola mundo")
console.print("Hola mundo", style="bold")
console.print("Hola mundo", style="bold green")
console.print("Hola mundo", style="bold green underline on red")

console.print("[bold green]Saludos[/bold green] [bold red]Terricolas[/bold red] :boom:")
```
Con el objeto instanciado `Console`, tenemos el método para sustituir el print. Con él, podemos darle formato a los strings que imprimamos, ya sea de color, tipo de letra o inclusive incluir emojis.

## Objeto Text
Podemos instanciar un objeto `rich.text.Text` el cual vamos a estilizar con varias opciones, para posteriormente imprimirlo en la consola:

```python
from rich.text import Text

text = Text("¡Los marcianos llegaron ya a la Tierra!")
text.stylize(style="bold red", start=5, end=14)
text.stylize(style="bold cyan", start=32, end=38)

console.print(text)
```

## Utilizar un Theme
Se puede utilizar un Theme personalizado, cuyo formato, nosotros podemos definir a nuestras necesidades:

```python
tema_personalizado = Theme({"exito": "italic green",
                            "error": "bold red",
                            "precaucion": "yellow blink"})

console = Console(theme=tema_personalizado)

console.print("Descarga completa", style="exito")
console.print("Actualización requerida", style="precaucion")
console.print("Recurso no encontrado", style="error")

console.print("Este mensaje [precaucion]parpadeará[/] todo el tiempo.")
```
La clase Theme recibirá un diccionario, cuyas `keys` serán las palabras claves que describirán el estilo. Y los `values` son los estilos descritos con la sintaxis de `Rich`.

## Emojis
Es posible utilizar emojis, ya sea declarando entre `: :` el nombre del emoji, o directamente insertandolos.

```python
console.print(":thumbs_up: ¡Descargado!")
console.print(":apple: :bug: 🥳 🤠 😍 🥰 😘 🫣 \n")
```
## Logs
Es posible imprimir logs sencillos con `console.log` para ir rastreando con formato legible lo que nuestro proceso va haciendo.

```python
for i in range(10):
    console.log(f"El proceso {i} inicializó.")
    time.sleep(0.25)
```

## Traceback
Es posible imprimir los traceback en un formato más bonito que el predeterminado. Para eso necesitaremos instalar el traceback

```python
from rich.traceback import install
install()
```
Con eso es suficiente, cada vez que se levante un error, el traceback se imprimirá de una forma muy bonita

Cuando usamos un bloque `try`-`except`, al capturar la excepción, podríamos imprimir el traceback sin la necesidad de interrumpir el programa con el siguiente instrucción:

```python
console.print_exception(show_locals=True)
```

## Exportar el output
Se puede exportar todo la salida que resultó de ejecutar el programa e imprimir por la consola.

Para esto, se debe indicar en la instanciación de la `Console` se le debe pasar la opción `record=True`.

```python
console = Console(record=True)
.
.
.
console.save_html("output.html")
```
Y después guardar toda la salida en algún archivo con el método `console.save_html`

## Tablas
Para desplegar información en tablas, se construyen con el objeto `rich.table.Table`, el cual se debe instanciar, agregar una a una las columnas, para posterior agregar una a una los renglones, como sigue:

```python
from rich.table import Table

# Instanciamos el objeto tabla. Agregamos un titulo y una lista.
table = Table(title="Lista de compras", title_style="bold cyan")

# Agregamos columnas, su nombre, el estilo del titulo de la columna y 
# estilo de los elementos de la columna
table.add_column("Producto", header_style="bold green", style="green")
table.add_column("Categoría", header_style="bold magenta", style="magenta", justify="center")
table.add_column("Precio", header_style="bold blue", style="blue", justify="right")

# Agregamos renglones con los elementos correspondientes de cada columna.
# Adiccionalmente se puede sobreescribir el estilo.
table.add_row("Manzanas", "Frutas", "$52.00")
table.add_row("Plátano macho frito", "Botanas", "$25.60", style="bold yellow")
table.add_row("Vino tinto del Valle de Guadalupe", "Vinos y Destilados", "$159.00", end_section=True)

table.add_section()

table.add_row("Galletas de chocolate", "Dulces", "$24.50")
table.add_row("Pan de muerto", "Panaderia", "$15.00")

console.print(table)
```
## Markdown
Se puede escribir Markdown básico para que sea desplegado en la consola. No despliega tablas ni LaTeX. Por lo que solo mostrará formato muy sencillo.

Debemos importar la siguiente clase:
```python
from rich.markdown import Markdown

documento = """
# Documentos en formato Markdown
* Listas
Y además acepta [hipervinculos](https://www.google.com)
"""
```
Debemos instanciar un objeto tipo Markdown con el string antes definido:

```python
md = Markdown(documento)
console.print(md)
```

## Barra de Progreso
También es posible agregar una barra de progreso sencilla:

```python
from rich.progress import track

for i in track(range(15), console=console, description="Descargando..."):
    time.sleep(0.25)

```
## Inspector de Objetos
Es posible inspeccionar objetos, esto es, que valores tiene sus atributos y que metodos continen, y desplegarlos de una forma sencilla y bien formateada:

```python
from rich import inspect
inspect(objeto, methods=True)
```

## Mensaje de estatus
Podemos imprimir un mensaje de que se está realizando alguna tarea, con una animación de que se está trabajando en algo. Se puede personalizar con el spinner (animación) favorita. Esto se realiza dentro de un bloque with y el objeto `Console.status`

```python
with console.status("[bold green]Working on tasks...", spinner="arrow3") as status:
    for i in range(10):
        console.log(f"El proceso {i} inicializó.")
        time.sleep(0.75)
```

# Referencias
* Documentación Oficial de [Rich](https://rich.readthedocs.io/en/stable/introduction.html).
* Repositorio en GitHub del [proyecto](https://github.com/Textualize/rich).
* [Supertutorial](https://www.youtube.com/watch?v=4zbehnz-8QU) en Youtube sobre Rich.
