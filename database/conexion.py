# ===========================================================
# ARCHIVO:    conexion.py
# FUNCION:    Gestion de conexion e inicializacion de la base de datos
# PROYECTO:   PMV Plataforma Legal - SENA ADSO
# VERSION: 2.3 (Correcion de Modulo)
# ===========================================================

# Importamos sqlite para poder crear y gestionar base de datos SQLite
import sqlite3

# IMportamos os para trabjar co rutas,carpetas y funciones del sitema operativo
import os

# Importamos la libreria "sys" para comunicarnos con el entorno
# donde se esta ejecutando Python. Esta libreria permite acceder
# a informacion del programa y controlar ciertos aspectos de su ejecucion,
# como recibir argumentos desde la terminal, mostrar errores
# o finalizar el programa manualmente
# El modulo sys en Python es una libreria interada que sirve para interactuar directamente
# con el sitema operativo y el interprete de Pyton
# Permite controlar la ejecucion del programa, leer datos desde la terminal y conocer
# informacion de la computadora donde corre el codigo
import sys

# ---- SECCION DE COMPATIBILIDAD DE RUTAS --------------------

# Guardamos en la variable "directorio_actual" la ruta completa
# de la carpeta donde se encuentra este archivo Python
#
# "__file__" representa el archivo actual
# "os.path.dirname()": es una funcion de la libreria integrada "os" que sirve para extraer la
#  ruta del directorio (carpeta) que contiene a un archivo especifico
# "os.patth.abspath()" obtiene su ruta absoluta: Es la ubicacion unica y exacta en la
# # computadora (ej. C:/Usuarios/Proyecto/mi_carpeta/datos.csv o /home/user/Proyecto/
# mi_carpeta/datos.csv)
# resultado: H:\Mi unidad\Plataforma_Legal\database
directorio_actual = os.path.dirname(os.path.abspath(__file__))
print("este es el directorio actual: ", directorio_actual)

# Obtenemos la carpeta raiz del proyecto
# "os.path.dirname()" toma la ruta de "directorio_actual"
# y devuelve la carpeta superior que la contiene
# resultado: H:\Mi unidad\Plataforma_Legal
directorio_raiz = os.path.dirname(directorio_actual)
print("Este es el directorio raiz del proyecto: ", directorio_raiz)

# Agregamos la carpeta raiz del proyecto a la lista de rutas Python
# Esto permite importar archivos o modulos que se encuentran
# en otras carpetas del proyecto
#
# "sys.path" sirve para añadir una carpeta a la lista de rutas donde
# Python busca modulos y paquetes para importar
# Al ejecutar esta linea, le indicas a Python que,
# ademas de buscar en sus carpetas internas,
# tambien revise dentro de directorio_raiz cuando escribas un import
sys.path.append(directorio_raiz)


# Intentemos importar los modulos usando diferentes rutas
# Esto permite que el programa funciones correctamente
# tanto si se ejecuta desde la raiz dell proyecto
# como si este archivo se ejecuta de manera independiente
try:
    #Forma 1: Cuando ejecutemos desde la raiz (app.py)

    # Importamos las constantes "RUTA_BD" y "RUTA_SCHEMA"
    # desde el archivo "config.py" que se encuentra
    # dentro de la carpeta "database"
    # Estas constantes almacenan las rutas de la base de datos
    # y del archivo de estructura SQL del proyecto
    from database.config import RUTA_BD, RUTA_SCHEMA

    # Importamos la clase "Usuario" desde el modulo "usuario"
    # que se encuentra dentro de la carpeta "logic"
    # Esta clase normalmente contiene la logica y las funciones
    # relacionadas con la gestion de usuarios en el sistema
    from logic.usuario import Usuario

# Si Python no encuentra alguno de los modulos importados,
# se genera el error "ModuleNotFoundError"
# Con "except" capturamos ese error para ejecutar
# una alternativa y evitar que el programa se detenga
except ModuleNotFoundError:


    # Forma 2: Cuando ejecutamos este archivo solo para pruebas

    # Si el archivo se ejecuta de forma independiente y Python
    # no encuentra la carpeta "database", importamos directamente
    # las constantes desde "config.py" ubicado en el mismo nivel
    # Esto sirve como una ruta alternativa para que el programa
    # siga funcionando correctamente durante pruebas o ejecuciones locales
    from config import RUTA_BD, RUTA_SCHEMA

    # Volvemos a importar la clase "Usuario" para asegurarnos
    # de que este disponible tambien en este metodo alternativo de importacion
    # Esto permite que el archivo funcione correctamente
    # incluso cuando se ejecuta de manera independiente
    from logic.usuario import Usuario

# --- SECCION 1: GESTION DE CONEXION ----------------------------------------

# Definimos una funcion llamada "obtener_Conexion"
# cuya tarea es crear y devolver una conexion con la base de datos SQLite
def obtener_conexion():


    # Usa la ruta del archivo .db definida en config.py
    # Utilizamos la ruta de la base de datos almacenada
    # en la constante "RUTA_BD", definida previamente en el archivo de configuracion
    # "sqlite3.connect()" abre la conexion con el archivo .db
    conexion = sqlite3.connect(RUTA_BD)

    # Configuramos la conexion para que los resultados
    # de las consultas se puedan manejar como diccionarios
    # Esto permite acceder a las columnas usando sus nombres en lugar de posiciones
    # numericas
    conexion.row_factory = sqlite3.Row

    # Devolvemos la conexion creada para poder utilizarla
    # en otras partes del programa
    return conexion

# -- SECCION 2: INICIALIZACION INTEGRADA -------------------------------------------

# Definimos la funcion "inicializar_bd"
# Su objetivo es crear la estructura de la base de datos
# ejecutando el archivo "schema.sql"
def inicializar_bd():

    # Creamos una conexion con la base de datos
    # utilizando la funcion definida anteriormente
    conexion = obtener_conexion()

    # Iniciamos un bloque "try" par intentar ejecutar
    # el proceso de inicializacion y poder manejar errores
    # en caso de que ocurran
    try:

        # Abrimos el archivo "schema.sql" en modo lectura ("r")
        # "encoding=´utf-8´" permite leer corectamente
        # caracteres especiales como tildes o simbolos
        # "with open(...)" asegura que el archivo se cierre
        # automaticamente al finalizar su uso
        with open(RUTA_SCHEMA, "r", encoding="utf-8") as archivo_sql:

            # Leemos todo el contenido del archivo SQL
            # y lo guardamos en la variable "script_sql"
            script_sql = archivo_sql.read()

            # Ejecutamos todas las instrucciones SQL contenidas
            # en el archivo, como la creacion de tablas
            # y configuraciones de la base de datos
            conexion.executescript(script_sql)

            # Guardamos los cambios realizados en la base de datos de forma permanente
            conexion.commit()

            # Mostramos un mensaje en consola indicando que la estructura de la base de datos
            # fue creada correctamente
            print(" Estructura de base de datos creada exitosamente")

            # Llama a la creacion del admin atomaticamente

            # Ejecutamso la funcion "_crear_administrador_interno()"
            # para crrear automaticamente un usuario administrador
            # en la base de datos
            # El nombre comienza con guion bajo (_) para indicar
            # que es una funcion de uso interno del modulo,
            # es decir, fue creada para ser utilizada solamente
            # dentro de este archivo y no desde otras partes del programa
            _crear_administrador_interno()

    # Capturamos cualquier error relacionado
    # con SQLite para evitar que el programa falle
    # y mostrar un mensaje mas claro
    except sqlite3.Error as error:

        # Mostramos el detalle del error ocurrido
        # durante la inicializacion de la base de datos
        print(f" Error al inicializar la base de datos: {error}")

    # El bloque "finally" se ejcuta siempre,
    # ocurra o no un error
    # Aqui cerreamos la conexioncon la base de datos
    # para liberar recursos y evitar problemas
    finally:

        # Cerramos la conexion activa con la base de datos
        conexion.close()

# -- SECCION 3: FUNCION AUXILIAR (INTERNA) ------------------------

# Definimos la funcion "_crear_administraor_interno()"
# El guion bajo () al inicio del nombre indica que esta funcion
# fue diseñada para uso interno del modulo, es decir.
# no deberia ser llamada directamente desde otros archivos
# Su objetivo es crear automaticamente un usuario administrador
# cuando el sistema inicia por primera vez
def _crear_administrador_interno() :

    # Creamos un nuevo objeto de la clase "Usuario"
    # Este onjeto almacenara toda la informacion
    # del administrador que sere registrado
    admin = Usuario()

    # Asignamos el nombre completo del administrador
    # Estos datos estan escritos directamente en el codigo,
    # por eso se conocen como "datos quemados" o datos fijos
    admin.nombre_completo = "Katherin Gomajoa"

    # Asignamos el correo electronico del administrador
    # Este correo servira como identificador unico dentro del sistema
    admin.correo_electronico = "benavideskate07@gmail.com"

    # Guardamos la contraseña en texto plano temporalmente
    # Normlamente, antes de almacenarla en la base de datos,
    # el sistema deberia cifrarla para mayor seguridad
    admin.contrasena_plana = "Legalis@2026"

    # Definimos el rol del usuario
    # El rol "ADMINISTRADOR" otorga permisos especiales para gestionar el sistema
    admin.rol = "ADMINISTRADOR"

    # Verificamos si el correo ya existe en la base de datos
    # "validar_unicidad_correo() comprueba si ya hay
    # unn usuario registrado con ese mismo correo
    # El "not" significa: " si el correo NO existe", entonces se puede crear
    if not admin.validar_unicidad_correo() :

        # Registramos el nuevo usuario administrador en la base de datos
        admin.registrar_usuario()

        # Mostramos un mensaje indicado
        # que el administrador fue creado correctamente
        print(" Administrados inicial creado con exito.")

    # Si el correo ya estaba registrado,
    # mostramos un mensaje informativo
    # para evitar crear usuarios duplicados
    else:

        # Informamos que el administrador
        # ya existia previamente en el sistema
        print(" El Administrador ya estaba registrado.")

# -- BLOQUE DE PRUEBA RAPIDA ---------------

# "__name__" es una variable especial de Python
# Cuando este archivo se ejecuta directamente,
# Python asigna el valor "_main_ a "_name_"
# Esto permite diferenciar si el archivo:
    # - Se ejcuta por si solo
    # - O si fue importado desde otro archivo
# Si ejecuta el arhivo directamente (ej. python mi_script.py):
    # Python le asigna el valor "_main_" a la varibale _name_
# Si el archivo es importado desde otro script (ej. import mi_script):
    # Python asigna a _name_ el nombre del archivo (sin la extension.py)
if __name__ == "__main__":

    # Llamamos a la funcion "inicializar_bd()"
    # para crear la estructura de la base de datos
    # y configurar el sistema al iniciar el programa
    inicializar_bd()
# ======================================================================