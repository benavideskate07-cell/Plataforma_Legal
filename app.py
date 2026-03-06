# =====================================================
# Archivo: app.py
# Proyecto: Legalis
# Descripcion: Punto de entrada de la aplicacion Flask.
# =====================================================

# Importa la clase Flask para crear la aplicacion web y la funcion render_template paa cargar y rendirizar plantillas HTML con Jinja2.
# Permite inicializar la app y mostrar vistas HTML dinamicas dentro de las rutas del proyecto
from flask import Flask,render_template # type: ignore

# Crea la instancia principal de la aplicacion Flask, usando el nombre del modulo para ubicar recursos y plantillas correctamente.
#Inicializa el servidor web y configura el contexto de la palicacion para menejar rutas, vistas y archivos estaticos
app = Flask(__name__)

# Define la ruta principal del sitio ("/") y la asocia a una funcion que atendera las solicitudes HTTP de inicio
# Indica que cuando un usuario accede a la URL raiz del proyecto, FLask ejecuta la funcion decorada para generar la respuesta correspondiente
@app.route("/")

# Define la funcion controladora que gestiona la vista de inicio cuando se accede a la ruta principal del sitio
# Actua como controlador: recibe la peticion del usuario desde la ruta / y retorna la respuesta que se mostrara en el navegador
def inicio():

    """Ruta principal del sistema Legalis.
    Procesa y renderiza la plantilla index.html mediante Jinja2
    Actua como pagina de inico (home) del sitio web Legalis y es la primera vista del usuario"""

    # Renderiza la plantilla index.html y la envia como respuesta al navegador para mostrar la pagina de inicio del sitio
    # Carga el archivo HTML desde la carpeta templates, procesa sus bloques dinamicos con Jinja2 y devuelve la vista al cliente
    return render_template("index.html")

# Verifica si el archivo se esta ejecutando directamente (no importado como modulo) para iniciar la aplicacion
#Garantiza que el servidor Flask se ejecute unicamente cuando este archivo sea el programa principal, evitando que se inicie automaticamente si es importado desde otro modulo
if __name__ == "__main__":

# Inicia el servidor de desarrollo de Flask en modo depuracion para mostrar errores detallados y recargar automaticamente los cambios
# Ejecuta la aplicacion de desarrollo de Flask en modo depuracion para mostrar errores en tiempo real y actualizar sin reiniciar manualmente el servidor
    app.run(debug=True)