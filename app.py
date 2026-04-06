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

# Verifica si el archivo se esta ejecutando directamente (no importa como modulo) para iniciar la aplicacion
#Garantiza que el servidor Flask se ejecute unicamente cuando este archivo sea el programa principal, evitando que se inicie automaticamente si es importado desde otro modulo

# Elemento: Decorador de ruta de Flask (@app.route)
#Comentario: Registra un punto de acceso (endpoint) en la aplicacion para la URL especifica "/preguntas"
# Funcion Tecnica: Mapea la direccion que el usuario escribe en su navegador hacia una funcion logica en el backend
# Diccionario: Decorador de ruta | Es el "GPS" del servidor | La ruta debe coincidir exactamente con el atributo "href" de tus enlaces en HTML
@app.route("/preguntas")

# Elemento: Definicion de funcion de Python (View Function)
# Comentaria Tecnico: Declara el bloque de contenido encargado de procesar la solicitud cuando se accede a la ruta definida
# Funcion Tecnica: Actua como el controlador que orquestara la respuesta que se le entrega al cliente
# DICCIONARIO: Funcion de Vista | Es el motor logico de la pagina | Se recomienda que el nombre de la funcion sea igual al nombre de la ruta para mayor claridad
def preguntas():

    # Elemento: Sentencia de retorno con funcion de renderizado de plantillas
    # Comentario Tecnico: Invoca el motor Jinja2 para procesar y enviar el archivo HTML "preguntas.html" al navegador
    # Funcion Tecnia: Conecta la logica del servidor con la interfaz visual (frontend) para mostrar la pagina final al usuario
    # DICCIONARIO: Renderizador | Transforma codigo estatico en paginas dinamicas | El archivo mencionado DEBE existir dentro de la carpeta "templates" del proyecto
    return render_template("preguntas.html")

# Elemento: Condiconal de ejecucion principal (Boilerplate)
# Comentario: Evalua la variable especial "_name_" para determinar si el script se esta ejecutando como el programa principal o si esta siendo importado como un modulo
# Funcion Tecnica: Actia como el interruptor de seguridad que autoriza el encendido del servicio Flask
# DICCIONARIO: Punto de entrada | Protege el codigo de ejecuciones accidentales en otros archivos | Es una convenccion obligatoria para scripts profesionales en Python
if __name__ == "__main__":

    # Elemento: Metodo de ejecucion de la instancia de la aplicacion Flask
    # Comentario Tecnico: Inicia el servidor web de desarrollo local en la direccion predeterminada (Usualmente localhost:5000) con el modo de depuracion activo
    # Funcion Tecnica: Pone al sistema en estado de "escucha" para recibir peticiones y reinicia el servidor automaticamente cada vez que guardas un cambio
    # DICCIONARIO: Arrancador de aplicacion | Permite probar la web en tiempo real y ver errores detalaldos en el navegador | El modo debug=true debe ser desactivado estrictamente antes de desplegar la web a un servidor de produccion
    app.run(debug=True)