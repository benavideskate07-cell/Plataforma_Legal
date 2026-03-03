# =====================================================
# Archivo: app.py
# Proyecto: Legalis
# Descripcion: Punto de entrada de la aplicacion Flask.
# =====================================================

from flask import Flask,render_template

#Inicializacion de la aplicacion
app = Flask(__name__)

@app.route("/") # Define una ruta web en Flask y la asocia a una funcion que atendera las peticiones a esa URL.

def inicio():
    """Ruta principal del sistema Legalis.
    Temporalmente renderiza la plantilla base para auditar 
    menu y footer antes de integrar la tienda."""

    return render_template("base.html")

if __name__ == "__main__":
# Arranque del servidor en modo desarrollo
    app.run(debug=True)