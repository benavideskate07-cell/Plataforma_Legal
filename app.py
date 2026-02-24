# Importamos la herramienta Flask para habilitar funciones de servidor web
from flask import Flask

#Creamos la aplicacion principal (instancia del motor web)
# *__name__* indica que el servidor se ejecutara desde este archivo
app = Flask(__name__)

# Definimos la ruta raiz o página de inicio con el símbolo */*
@app.route("/")
def inicio():
    # Esta función devuelve el mensaje que el ciudadano verá en su navegador
    return "Bienvemido a la Plataforma Legal de Tutelas - Servidor Opertivo"

# Bloque de seguridad para iniciar el servidor
if __name__ == "__main__":
    # Activamos el modo debug para detectar errores y refrescar cambios automaticamente
    app.run(debug=True)