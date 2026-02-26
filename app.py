# Importamos la herramienta Flask para habilitar funciones de servidor web
from flask import Flask,render_template

#Creamos la aplicacion principal (instancia del motor web)
# *__name__* indica que el servidor se ejecutara desde este archivo
app = Flask(__name__)

# Definimos la ruta raiz o página de inicio con el símbolo */*
@app.route("/")
def inicio():
    # CAMBIO REALIZADO: En lugar de texto, devolvemos el archivo HTML
    # Flask buscara "index.html" automaticamente dentro de la carpeta "templates"
    return render_template("index.html")

# Bloque de seguridad para iniciar el servidor
if __name__ == "__main__":
    # Activamos el modo debug para detectar errores y refrescar cambios automaticamente
    app.run(debug=True)