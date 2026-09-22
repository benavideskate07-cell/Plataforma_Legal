# =====================================================
# Archivo: app.py
# Proyecto: Legalis
# Descripcion: Punto de entrada de la aplicacion Flask.
# =====================================================

# ========================================================
# ARCHIVO: app.py
# FUNCION: Impotacion de librerias base del framework
# ========================================================

# Elemento: Librerias principales de Flask
# Funcion:
# - Flask: crea la aplicacion web
# - render_template: renderiza vistas HTML
# - request: captura datos enviados por el cliente
# - redirect y url_for: gestionan redirecciones entre rutas
# - flash: muestra mensajes temporales al usuario
# - session: administra la sesion del usuario autenticado
from flask import Flask,render_template, request, redirect, url_for, flash, session # type: ignore

# =====================================================
# IMPORTS - INCREMENTO: REGISTRAR CLIENTE
# =====================================================

# Elemento: Configuracion de Base de Datos
# Funcion: Importa las rutas necesarias para acceder a la base
# de datos y al esquema SQL utilizado durante la
# inicializacion del sistema
from database.config import RUTA_BD, RUTA_SCHEMA

# Elemento: inicializar_bd
# Funcion: Ejecuta la creacion de la estructura inicial de la
# base de datos a partir del esquema SQL definido por
# el sistema, garantizando la disponibilidad de las
# tablas requeridas para la operacion de Legalis
from database.conexion import inicializar_bd

# Elemento: Usuario
# Funcion: Importa la entidad de logica de negocio responsable
# de encapsular los procesos relacionados con la gestion
# de usuarios, tales como registro, inicio de sesion,
# validaciones de datos, verificacion de credenciales y
# carga de informacion del perfil
from logic.usuario import Usuario

# Elemento: app
# Funcion: Instancia principal del framework Flask. Representa
# la aplicacion web legalis y centraliza ña configuracion,
# definicion de rutas, gestion de peticiones y ejecucion del servidor web
app = Flask(__name__)

# Elemento: secret_key
# Funcion: Define la clave secreta utilizada por Flask para
# proteger la integridad de las sesiones de usuario,
# firmar cookies y garantizar la seguridad de los datos
# almacenados durante la navegacion
# Observacion tecnica: En un entorno de produccion, esta clave no deberia estar escrita
# directamente en el codigo fuente. lo recomendable es almacenarla en variables de entorno o # archivos de configuracion protegidos
app.secret_key = 'Legalis@SENA@2026#PMV'

# Elemento: Inicializaciaon de la Base de datos
# Funcion: Al iniciar la aplicacion, se crea un contexto
# Flask para ejecutar la configuracion inicial de la
# base de datos, garantizando la existencia de las
# tablas y estructuras necesarias para la operacion
# del sistema
with app.app_context() :
    inicializar_bd()

# ================================================================
# RUTAS - INCREMENTO: REGISTRAR CLIENTE
# ================================================================

# Elemento: Decorador de Ruta Flask
# Funcion:
# - "/registro": URL asociada al proceso de registro de usuarios
# - "GET": Renderiza el formulario de registro
# - "POST": Recibe, valida y procesa los datos enviados por el
# usuario para crear una nueva cuenta en el sistema
# -"@app-route()": Vincula la funcion que sigue al endpoint
# correspondiente dentro de la aplicacion Flask
@app.route('/registro', methods=['GET', 'POST'])

# "def": Palabra reservada de Python utilizada para definir una funcion
# registro: nombre o identificador de la funcion
# Al estar asociada al decorador @app.route("/regsitro")
# tambien corresponde al nombre del endpoint que Flask
# utiliza para identificar esta ruta
# "()". parentesis que indican los parametros de la funcion
# En este caso estan vacios porque la funcion no recibe
# argumentos directamente desde la URL
# ":": indica el inicio del bloque de instrucciones
# pertenecientes a la funcion
# la intruccion define la funcion "registro", que contiene la
# logica encagada de procesar las solicitudes realizadas sobre
# la ruta /registro
def registro() :

    # request: objeto de Flask que contien la informacion de la
    # solicitud HTTP enviada por el cliente
    # method: atributo del objeto request que indica el metodo HTTP
    # utilizado para realizar la peticion ("GET","POST", "PUT", "DELETE", etc)
    # get: metodo http utilizad para solicitar recursos o paginas
    # al servidor sin enviar informacion para su procesamiento
    # la instruccion verifica si la solicitud recibida corresponde
    # a una peticion http de tipo get para ejecutar la logica
    # asociada a la visibilizacion inicial de la pagina o formulario
    if request.method == 'GET':
        return render_template('registro.html')

    # request: objeto de Flask que contien la informacion de la
    # solicitud HTTP enviada por el cliente
    # method: atributo del objeto request que indica el metodo HTTP
    # utilizado para realizar la peticion ("GET","POST", "PUT", "DELETE", etc)
    # post: metodo http empleado para enviar datos al seidor
    # con el proposito de ser procesados o almacenados
    # la instruccion verifica si la solicitud recibida corresponde
    # a una peticion http de tipo post lo que indica que el usuario
    # ha enviado informacion desde un formulario u otro mecanismo de captura de datos
    if request.method == 'POST' :

        # "Usuario": Clase importada desde el módulo logic.usuario que
        # representa el modelo de usuario dentro del sistema.
        # "()": Constructor de la clase Usuario utilizado para crear una
        # nueva instancia de la clase.
        # "usuario": Variable que almacena la referencia al objeto Usuario
        # creado en memoria.
        # La instrucción instancia la clase Usuario, inicializa sus
        # atributos definidos en "__init__()" y permite utilizar sus
        # metodos y propiedades durante el proceso de registro
        usuario = Usuario()

        # usuario: Objeto instanciado de la clase Usuario que almacena
        # y gestiona la información relacionada con el usuario.
        # "nombre_completo": Atributo del objeto Usuario destinado a
        # almacenar el nombre completo del usuario.
        # "request.form": Colección de datos enviados mediante un formulario
        # HTML utilizando el método "HTTP POST".
        # get(): Método que recupera el valor asociado a una clave dentro
        # del formulario. Si la clave no existe, retorna el valor
        # por defecto especificado como segundo parámetro.
        # "('nombre_completo', ''): # Busca el campo 'nombre_completo' dentro de los datos 
        # enviados por el formulario. Si el campo no existe, retorna una cadena
        # vacía ('') para evitar errores durante el procesamiento.
        # strip(): Método de cadena que elimina espacios en blanco al 
        # inicio y al final del texto.
        # upper(): Método de cadena que convierte todos los 
        # caracteres alfabéticos a mayúsculas.
        # La instrucción obtiene el nombre completo enviado desde el
        # formulario, elimina espacios innecesarios, lo convierte a
        # mayúsculas y lo asigna al atributo nombre_completo del usuario.
        usuario.nombre_completo = request.form.get('nombre_completo', "").strip().upper()
        usuario.correo_electronico = request.form.get('correo_electronico', "").strip().upper()
        usuario.confirmar_correo = request.form.get('confirmar_correo', "").strip().upper()
        usuario.contrasena_plana = request.form.get('contrasena', "")
        usuario.confirmar_contrasena = request.form.get('confirmar_contrasena', "")
        usuario.rol ="CLIENTE"

        # Se maniene su logica original que aprovecha el "on" / None de HTML
        usuario.aceptacion_terminos = request.form.get('aceptacion_terminos')

        # usuario: Instancia de la clase Usuario que contiene los datos
        # capturados desde el formulario de registro.
        # validar_obligatoriedad(): Método que verifica que los campos
        # obligatorios del objeto Usuario contengan información
        # válida y no se encuentren vacíos.
        # obligatorio: Variable que recibe el resultado de la validación.
        # Generalmente contiene un valor booleano:
        # True si la validación es exitosa, False en caso contrario.
        # vacio: Variable que recibe el mensaje asociado al resultado de
        # la validación, normalmente indicando qué campo obligatorio
        # no cumple la condición requerida.
        # La instrucción ejecuta la validación de obligatoriedad y almacena
        # el resultado y el mensaje retornados por el método.
        obligatorio, vacio= usuario.validar_obligatoriedad()

        # not: Operador logico de negacion que invierte el valor de una
        # expresion boolena. Convierte True en False y False en True
        # obligatorio: Variable boolena que contiene el resultado de la
        # validacion de obligatoriedad realizada previamente
        # La instruccion verifica si la validacion de campos obligatorios
        # ha fallado. Si obligatorio es False, la condicion se evalua
        # como True y se ejecuta el bloque condicional
        if not obligatorio:

            # "flash()": Funcion de Flask que almacena mensajes temporales
            # en la sesion para mostrados al usuario en la siguiente respuesta http
            # vacio: Variable que contiene el mensaje generado por el proceso de validacion
            # "excepcion": Categoria o tipo del mansaje flash utilizada por la interfaz
            # para aplicar formato visual o comportamiento especifico
            # la instruccion registra un mensaje temporal de error para
            # informar al usuario el resultado de la validacion
            flash(vacio, 'excepcion')

            # "return": Palabra reservada de Python utilizada para finalizar
            # la ejecucion de la funcion actual y devolver un valor
            # o una respuesta al codigo que realizo la llamada
            # "redirect()": Funcion de Flask que genera una respuesta HTTP de
            # redireccion para enviar al navegador hacia otra URL
            # "url_for": Funcion de Flask que genera dinamicamente la URL
            # correspondiente a un endpoint registrado
            # "regsitro": Nombre del endpoint asociado a la funcion "regsitro"
            # la instruccion genera la URL del endpoint "registro", crea una
            # respuesta de redireccion HTTP y la devuelve al navegador
            # Como resultado, el usuario es enviado nuevamente a la ruta
            # "/registro"
            return redirect(url_for('registro'))

        # usuario: Instancia de la clase Usuario que contiene los datos
        # capturados desde el formulario de registro
        # "validar_formato_correo": Metodo de la clase Usuario que verifica
        # si el correo electronico cumple el formato basico
        # requerido por el sistema. En la implementacion actual,
        # comprueba la presencia del caracter "@"
        # formato: Variable que recibe el resultado booleano retornado por el metodo
        # True: El formato del correo es valido
        # False: El formato del correo no es valido
        # "no valido": Variable que recibe el segundo valor retornado por el metodo
        # - None: cuando la validacion es correcta
        # - Mensaje de error: cuando la validacion falla
        # "formato, no_valido": Utilizan asignacion multiple para
        # desempaquetar los dos valores retornados para validar_formato_correo
        # La instruccion ejecuta la validacion del formato del correo y
        # almacena por separado el resultado de la validacion y el mensaje correspondiente
        formato, no_valido= usuario.validar_formato_correo()

        # not: Operador logico de negacion que invierte un valor booleano
        # formato: Variable que contiene el resultado de la validacion
        # La instruccion verifica si el resultado de la validacion es False
        # Si formato es False, "not formato" se evalua como True y se
        # ejecuta el bloque condicional
        if not formato:

            # "flash": Funcion de Flash que almacena temporalmente un
            # mensaje en la sesion para ser posteriormente por plantilla
            # "no_valido": Variable que contien el mensaje de error retornado
            # por validar_formato_correo
            # "excepcion": Categoria asignada al mensaje flash para
            # identificarlo como una notificacion de error
            # La instruccion alamacena temporalmente el mensaje de validacion
            # para mostrarlo al usuario en la interfaz
            flash(no_valido, 'excepcion')

            # "flash": Funcion de Flask que almacena temporalmente un
            # mensaje en la sesion para ser recuperado posteriormente por la plantilla
            # "no_valido": VVariable que contiene el mensaje de error retornado
            # por "validar_formato_correo"
            # "excepcion": Categoria asignada al mensaje flash para
            # identificarlo como una notificacion de error
            # La instruccion almacena temporalmente el mensaje de validacion
            # para mostrarlo al usuario en la interfaz
            return redirect(url_for('registro'))

        # usuario: Instancia de la clase Usuario que contiene los datos
        # capturados desde el formulario de registro
        # "validar_coincidencia": Metodo de la clase Usuario que compara
        # el correo electronico con su confirmacion y la contraseña
        # con su respectiva confirmacion
        # coincidencia: Variable que recibe el resultado booleano retornado
        # por el metodo
        # - True: los valores comparados coinciden
        # - False: al menos uno de los valores coinciden
        # "no_coinciden": Variable que recibe el segudo valor retornado
        # por el metodo
        # - None: cuando las comparaciones son correctas
        # - Mensaje de error: cuando existe una diferencia
        # "coincidencia, no_coinciden": Utilizan asignacion multiple para
        # desempaquetar los dos valores retornado por el metodo
        # La instruccion ejecuta la validacion de coincidencia y alamacena
        # por separado el resultado de la comparacion y el mensaje asociadao
        coincidencia, no_coinciden=usuario.validar_coincidencia()

        # not: Operador logico de negacion que invierte un valor booleano
        # de la operacion evaluada
        # formato: Variable que contiene el resultado de la validacion
        # La instruccion verifica si la comparacion fallo. Si coincidencia
        # es False, "not coincidencia" se evalua como True y se
        # ejecuta el bloque condicional
        if not coincidencia:

            # "flash": Funcion de Flash que almacena temporalmente un
            # mensaje en la sesion para ser posteriormente por plantilla
            # "no_coinciden": Variable que contien el mensaje de error retornado
            # por validar_coincidencia cuando existe una diferencia
            # "excepcion": Categoria asignada al mensaje flash para
            # identificarlo como una notificacion de error
            # La instruccion alamacena temporalmente el mensaje de validacion
            # para mostrarlo al usuario en la interfaz
            flash(no_coinciden, 'excepcion')

            # "redirect": Funcion de Flask que generea una respuesta HTTP
            # de redireccion hacia otra ruta
            # "url_for" Funcion que genera dinamicamente la URL asociada
            # al endpoint indicado
            # "registro": Nombre del endpoint correspondiente a la "registro"
            # "return": Finaliza la ejecucion de la funcion actual y devuelve
            # la respuesta de redireccion
            # La instruccion redirige al usuario nuevamente al formulario
            # de registro para corregir los datos que coinciden
            return redirect(url_for('registro'))

        # usuario: Instancia de la clase Usuario que contiene los datos
        # capturados desde el formulario de registro.
        # "validar_long_contrasena()": Método de la clase Usuario que verifica
        # la longitud de la contraseña almacenada en contrasena_plana.
        # La validación comprueba que tenga al menos 8 caracteres.
        # longitud: Variable que recibe el primer valor retornado por el método.
        # - True → la contraseña cumple la longitud mínima.
        # - False → la contraseña tiene menos de 8 caracteres.
        # muy_corta: Variable que recibe el segundo valor retornado por el método.
        # - None → cuando la validación es correcta.
        # - Mensaje de error → cuando la contraseña no cumple la longitud mínima.
        # longitud, muy_corta: Utilizan asignación múltiple para
        # desempaquetar los dos valores retornados por el método.
        # La instrucción ejecuta la validación de longitud de la contraseña
        # y almacena por separado el resultado de la validación y el mensaje asociado.
        longitud, muy_corta=usuario.validar_long_contrasena()

        # not: Operador lógico de negación que invierte el valor booleano
        # de la expresión evaluada.
        # longitud: Variable que contiene el resultado de la validación.
        # La instrucción verifica si la contraseña NO cumple la longitud
        # mínima requerida. Si longitud es False, "not longitud" se evalúa
        # como True y se ejecuta el bloque condicional.
        if not longitud:

            # flash(): Función de Flask que almacena temporalmente un
            # mensaje en la sesión para que pueda ser recuperado
            # posteriormente por la plantilla.
            # "muy_corta": Variable que contiene el mensaje de error retornado
            # por "validar_long_contrasena()".
            # "'excepcion'": Categoría asignada al mensaje flash para
            # identificarlo como una notificación de error.
            # La instrucción almacena temporalmente el mensaje generado
            # por la validación para mostrarlo al usuario
            flash(muy_corta, 'excepcion')

            # redirect(): Función de Flask que genera una respuesta HTTP
            # de redirección hacia otra ruta.
            # "url_for()": Función de Flask que genera dinámicamente la URL
            # correspondiente al endpoint indicado.
            # "'registro'": Nombre del endpoint asociado a la función registro().
            # "return": Finaliza la ejecución de la función actual y devuelve
            # la respuesta de redirección.
            # La instrucción redirige nuevamente al formulario de registro
            # para que el usuario pueda corregir la contraseña.
            return redirect(url_for('registro'))

        # validar_unicidad_correo(): Método que ejecuta una consulta SQL
        # sobre la tabla de usuarios para comprobar la existencia previa del
        # correo electrónico registrado en el objeto Usuario.
        # existe: Variable booleana que almacena el resultado retornado por el método.
        # La instrucción invoca el método de validación y almacena el
        # resultado de la consulta para su posterior evaluación en una estructura condicional.
        existe= usuario.validar_unicidad_correo()

        # if: Estructura condicional que ejecuta el bloque de código
        # únicamente cuando la expresión evaluada es True.
        # La instrucción verifica si el correo electrónico ya existe
        # en el sistema para impedir la creación de cuentas duplicadas.
        # existe: Variable booleana que contiene el resultado de la
        # validación de unicidad del correo electrónico.
        # True indica que el correo ya se encuentra registrado
        # en la base de datos; False indica que está disponible.
        if existe:

            # flash(): Función de Flask que almacena mensajes temporales
            # en la sesión del usuario para ser mostrados en la
            # siguiente respuesta HTTP.
            # 'El Correo electrónico ya se encuentra registrado...':
            # Mensaje informativo que será presentado al usuario.
            # 'excepcion': Categoría asociada al mensaje flash, utilizada
            # por la interfaz para aplicar estilos visuales
            # o identificar el tipo de notificación.
            # La instrucción registra un mensaje de alerta indicando que
            # el correo electrónico ya está registrado en el sistema.
            flash("El Correo elctronico ya se encuentra registrado, ingrese uno diferente", 'excepcion')

            # "redirect()": Función que genera una respuesta HTTP de
            # redirección hacia otra ruta de la aplicación.
            # "url_for()": Función que construye dinámicamente la URL de
            # un endpoint registrado en Flask.
            # "'registro': Nombre del endpoint asociado al formulario de
            # registro de usuarios.
            # "return": Finaliza la ejecución de la función actual y
            # devuelve la respuesta de redirección al cliente.
            # La instrucción redirige al usuario nuevamente al formulario
            # de registro para que ingrese un correo diferente.
            return redirect(url_for('registro'))

        # else: Bloque alternativo de una estructura condicional.
        # Se ejecuta únicamente cuando la condición evaluada
        # en el if anterior resulta False.
        # En este caso, significa que el correo electrónico no existe
        # en la base de datos y el proceso de registro puede continuar.
        else:

            # usuario: Instancia de la clase Usuario que contiene los
            # datos validados del formulario.
            # "registrar_usuario()"": Método que inserta un nuevo registro
            # en la tabla usuarios de la base de datos.
            # El método retorna:
            # - True → registro exitoso.
            # - False → error durante la inserción.
            # exito: Variable booleana que almacena el resultado del
            # proceso de registro.
            # La instrucción ejecuta el proceso de persistencia del
            # usuario y almacena el resultado de la operación.
            exito=usuario.registrar_usuario()

            # not: Operador logico que invierte el valor booleano
            # de la expresion evaluada
            # exito: Variable que contiene el resultado retornado
            # por registrar_usuario
            # La instruccion verifica si ocurrio un error durante
            # el proceso de insercion en la base de datos
            if not exito:

                # flash(): Función de Flask que almacena mensajes
                # temporales en la sesión del usuario para ser mostrados en la
                # siguiente respuesta HTTP.
                # 'excepcion': Categoría asociada al mensaje flash
                # La instrucción registra una notificacion de error
                # para informar que el registro no pudo completarse
                flash("Error de conexion con el servidor. Por favor intente mas tarde", 'excepcion')

                # "redirect()": Función que genera una respuesta HTTP
                # "url_for()": Construye  la URL asociada al endpoint indicado
                # "'registro': Endpoint correspondiente al formulario de registro
                # "return": Finaliza la ejecución de la función actual y
                # devuelve la respuesta de redirección al cliente.
                # La instrucción redirige al usuario nuevamente a la pagina
                # de registro para intentar el proceso mas tarde.
                return redirect(url_for('registro'))

            # else: Se ejcuta cuando exito contiene el valor True,
            # indicando que el usuario fue registrado correctamente
            # en la base de datos
            else:

                # "flash": Almacena un mensaje temporal de confirmacion
                # "exito": Categoria utilizada para identificar mensajes
                # de operacion exitosa en la interfaz
                # La instruccion regsitra una notificacion informando que
                # el usuario fue creado correctamente
                flash("!Registro exitoso! Ya puedes iniciar sesion.", 'exito')

                # " render_template()": Funcion de Flask  que procesa una
                # plantilla HTML y genera la respuesta
                # que sera enviada al navegador
                # "registro.html": Archivo de plantilla ubicado en el
                # directorio templates
                # "return": Finaliza la ejecucion de la funcion y devuleve
                # el contenido HTML generado
                # La instruccion renderiza nuevamente la vista de registro
                # para mostrar el mensaje de confirmacion al usuario
                return render_template('registro.html')

# ================================================================
# RUTA: INICIO- INDEX
# ================================================================

@app.route("/")
def inicio():
    return render_template("index.html")

# ================================================================
# RUTA: PREGUNTAS FRECUENTES
# ================================================================

# "@app.rour": Decorador de Flask utilizado para registrar una
# regla de enrutamiento dentro de la aplicacion
# "/preguntas": Ruta o URL asociada a la vista de preguntas frecuentes
# La instruccion vincula la URL /preguntas con la funcion
# "preguntas", permitiendo que Flask invoque dicha funcion cuando
# recibe una solicitud HTTP dirigida a esta ruta
@app.route("/preguntas")

# "def": Palabra reservada de Python utilizada para definir una funcion
# preguntas: Nombre de la funcion y nombre del endpoint que Flask
# utilizara para identificar esta ruta
# "()": Indica que la funcion no recibe parametros directamente
# La funcion contiene la logica que procesa la solicitud realizada
# sobre la ruta "/preguntas"
def preguntas():

    # "return": Palabra reservada de Python que finaliza la ejecucion
    # de la funcion y devuelve una respuesta al cliente
    # "render_template": Funcion de Flask que busca una plantilla
    # HTML dentro del directorio "templates",
    # procesa mediante Jinja2 y genera una
    # respuesta HTML
    # "preguntas.html": Nombre del archivo de plantilla que contiene
    # el contenido de la vista de preguntas
    # La instruccion procesa la plantilla "preguntas.html" y devuelve
    # el HTML generado como respuesta HTTP al navegador
    return render_template("preguntas.html")

# ==============================================================
# RUTA: QUIENES SOMOS (IDENTIDAD INSTITUCIONAL)
# ==============================================================

# "@app.route": Decorador de Flask utilizado para registrar una
# regla de enrutamiento dentro de la aplicacion
# "/nosotros": Ruta o URL asociada a la vista institucional "Quienes somos"
# La instruccion vincula la URL "/nosotros" con la funcion
# "nosotros" permitiendo que Flask invoque dicha funcion cuando
# recibe una solicitud HTTP dirgida a esta ruta
@app.route("/nosotros")

# def: Palabra reservada de Python utilizada para definir una funcion
# nosotros: Nombre de la funcion y nombre del endpoint que Flask
# utilizara para identificar esta ruta
# "()": Indica que la funcion no recibe parametros directamente
# La funcion contiene la logica que procesa la solicitud realizada
# sobre la ruta "/nosotros"
def nosotros ():

    # "return": Palabra reservada de Python que finaliza la ejecucion
    # de la funcion y devuelve una respuesta al cliente
    # "render_template": Funcion de Flask que busca una plantilla
    # HTML dentro del directorio "templates",
    # procesa mediante Jinja2 y genera una
    # respuesta HTML
    # "preguntas.html": Nombre del archivo de plantilla que contiene
    # el contenido de la vista de preguntas
    # La instruccion procesa la plantilla "nosotros.html" y devuelve
    # el HTML generado como respuesta HTTP al navegador
    return render_template("nosotros.html")

# ====================================================
# RUTA: POLITICA DE PRIVACIDAD (LEGAL)
# ====================================================

# "@app.route": Decorador de Flask utilizado para registrar una
# regla de enrutamiento dentro de la aplicacion
# "/privacidad": Ruta o URL asociada a la vista que contiene la
# politica de privacidad del sistema
# La instruccion vincula la URL "/privacidad" con la funcion
# "privacidad()" permitiendo que Flask invoque dicha funcion cuando
# recibe una solicitud HTTP dirgida a esta ruta
@app.route("/privacidad")

# def: Palabra reservada de Python utilizada para definir una funcion
# privacidad: Nombre de la funcion y nombre del endpoint que Flask
# utilizara para identificar esta ruta
# "()": Indica que la funcion no recibe parametros directamente
# La funcion contiene la logica que procesa la solicitud realizada
# sobre la ruta "/privacidad"
def privacidad():

    # "return": Palabra reservada de Python que finaliza la ejecucion
    # de la funcion y devuelve una respuesta al cliente
    # "render_template": Funcion de Flask que busca una plantilla
    # HTML dentro del directorio "templates",
    # procesa mediante Jinja2 y genera una
    # respuesta HTML
    # "privacidad.html": Nombre del archivo de plantilla que contiene
    # el contenido de la vista de preguntas
    # La instruccion procesa la plantilla "privacidad.html" y devuelve
    # el HTML generado como respuesta HTTP al navegador
    return render_template("privacidad.html")

# ==============================================================
# RUTA: TERMINOS Y CONDICIONES (LEGAL)
# ==============================================================

# "@app.route": Decorador de Flask utilizado para registrar una
# regla de enrutamiento dentro de la aplicacion
# "/terminos": Ruta o URL asociada a la vista que contiene la
# politica de privacidad del sistema
# La instruccion vincula la URL "/terminos" con la funcion
# "terminos()" permitiendo que Flask invoque dicha funcion cuando
# recibe una solicitud HTTP dirgida a esta ruta
@app.route("/terminos-y-condiciones")

# def: Palabra reservada de Python utilizada para definir una funcion
# terminos: Nombre de la funcion y nombre del endpoint que Flask
# utilizara para identificar esta ruta
# "()": Indica que la funcion no recibe parametros directamente
# La funcion contiene la logica que procesa la solicitud realizada
# sobre la ruta "/terminos"
def terminos() :

    # "return": Palabra reservada de Python que finaliza la ejecucion
    # de la funcion y devuelve una respuesta al cliente
    # "render_template": Funcion de Flask que busca una plantilla
    # HTML dentro del directorio "templates",
    # procesa mediante Jinja2 y genera una
    # respuesta HTML
    # "privacidad.html": Nombre del archivo de plantilla que contiene
    # el contenido de la vista de preguntas
    # La instruccion procesa la plantilla "terminos.html" y devuelve
    # el HTML generado como respuesta HTTP al navegador
    return render_template("terminos.html")

# ==============================================================
# RUTA: Temporales
# ==============================================================

@app.route("/ingreso")
def ingreso():
        return render_template("base.html")

@app.route("/recuperar")
def recuperar() :
    return render_template("base.html")

# ===========================================================

# "__name__": Variable especial de Python que contiene el nombre
# del modulo que se esta ejecutando
# Cuando el archivo se ejecuta directamente, su valor
# es "__main__"
# "==": Operador de comparacion que verifica si dos valores son iguales
# "__main__": Valor asignado a __name__ cuando este archivo es
# ejecutado directamente por Python
# "if": Estructura condicional que permite ejecutar un bloque de
# codigo unicamente cuando la condicion evaluada es verdadera
# La instruccion verifica si el archivo actual esta siendo
# ejecutado directamente y no importado como modulo desde otro
# archivo
if __name__ == "__main__":

    # "app": Instancia principal de la aplicacion Flask creada
    # anteriormente mediante Flask(__name__)
    # "run": Metodo de la instancia Flask utilizado para iniciar
    # el servidor web de desarrollo
    # "debug": Parametro de configuracion de Flask que activa el
    # modo de depuracion cuando su valor es True
    # En este modo, Flask puede mostrar informacion
    # detallada de errores y reiniciar automaticamente
    # el servidor cuando detecta cambios en el codigo
    # "True": Valor booleano que activa la opcion de depuracion
    # La instruccion inicia el servidor de desarrollo de Flask
    # cuando el archivo se ejecuta directamente
    app.run(debug=True)