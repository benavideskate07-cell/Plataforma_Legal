# ================================================================
# ARCHIVO: usuario.py
# FUNCION: Modelo de Usuario con validaciones y persistencia
# PROYECTO: PMV Plataforma Legal - SENA ADSO
# VERSION: 2.1 (Redefinido) (cite:25, 27)
# ================================================================

# Importamos la libreria "sqlite3" para poder trabajar
# con bases de datos SQLite desde Python
# Esta libreria permite:
    # - Crear conexiones con archivos .db
    # - Ejecutar consultas SQL
    # - Insertar, modificar y consultar datos
    # - Manejar errores relacionados con la base de datos
import sqlite3

# Importamos las funciones "generate_password_hash" y "check_password_hash"
# desde el modulo de seguridad de Werkzeug
# "generate_password_hash" convierte una contraseña en hash seguro
# "check_password_hash" compara una contraseña en texto plano
# contra un hash ya guardado, sin necesidad de revertir el cifrado
from werkzeug.security import generate_password_hash, check_password_hash


# Definimos la clase "Usuario"
# Una clase funciona como un molde o plantilla
# para crear objetos con caracteristicas y comportamientos similares
# En este caso, la clase "Usuario" representa
# la informacion y funcionalidades de un usuario del sistema
class Usuario:

    # Definimos el metodo especial "__init__"
    # Este metodo se ejecuta automaticamente
    # cada vez que se crea un nuevo objeto de la clase
    # Su funcion principal es inicializar los atributos del usuario
    def __init__(self):

        # "self" representa el objeto actual que se esta creando
        # Guardamos el nombre completo del usuario
        # Inicialmente se asigna una cadena vacia
        self.nombre_completo = ""

        # Guardamos el identificador unico del usuaario
        # Se inicializa en None porque este valor no lo asgna
        # el aprendiz - lo genera automaticamente la base de datos
        # (AUTOINCREMENT) y solo se conoce despues de una consulta
        self.id = None

        # Guardamos el correo electronico del usuario
        # Este dato normalmente se utilizara para identificar al usuario en el sistema
        self.correo_electronico = ""

        # Variable utilizada para confirmar
        # que el correo fue escrito correctamente
        # El usuario debera ingresar nuevamente el correo
        # y luego ambos valores seran comparados
        self.confirmar_correo = ""

        # Almacenamos temporalmente la contraseña
        # escrita por el usuario
        # Se llama "plana" porque aun no ha sido cifrada
        # o convertida en un hash de seguridad
        # Despues sera transformada en una version segura
        # antes de guardarse en l base de datos
        self.contrasena_plana = ""

        # Variable utilizada para confirmar
        # la contraseña ingresada por el usuario
        # Esto ayuda a reducir errores de escritura durante el registro
        self.confirmar_contrasena = ""

        # Guaradamos el rol del usuario dentro del sistema
        # El rol define los permisos y funciones
        # que tendra el usuario, por ejemplo: ADMINISTRADOR, CLIENTE O EMPLEADO
        self.rol = ""

        # Variable booleana que indica si el usuario
        # acepto los terminos y condiciones
        # "False" significa que aun no los ha aceptado
        # Mas adelante cambiara a "True" cuando el usuario
        # marque la opcion correspondiente
        self.aceptacion_terminos = False

    # - SECCION 2: VALIDACIONES DE INTEGRIDAD ---------------

    # Explicacion: Verificamos que los datos cumplan las reglas del negocio

    # Definimos el metodo "validar_obligatoriedad"
    # Este metodo verifica que todos los campos
    # obligatorios del formulario lo hayan sido comletados
    # Si algun dato falta, la funcion devuelve:
        # - False - indicando que la validacion fallo
        # - Un mensaje de alerta explicando el problema
    def validar_obligatoriedad(self):

        # ".strip()" elimina espacios vacios al inicio y al final del texto
        # Luego "len(...)" cuenta la cantidad de caracteres restantes
            # Si el resultado es 0, significa que el usuario
            # no escribio ningun nombre valido
        if len(self.nombre_completo.strip()) == 0:

            # Retornamos:
                # - False- indicando que la validacion fallo
                # - Un mensaje explicando el error encontrado
            return False, "[ALERTA] Bloqueado: El nombre completo es obligatorio"

        # Verificamos que el correo electronico no este vacio
        if len(self.correo_electronico.strip()) == 0:

            # Mostramos una alerta si el usuario no ingreso el correo electronico
            return False, "[ALERTA] Bloqueado: El correo electronico es obligatorio"

        # Verificamos que el usuario haya escrito el correo de confirmacion
        if len(self.confirmar_correo.strip()) == 0:

            # Mostramos un mensaje indicando que debe confirmar el correo electronico
            return False,"[ALERTA] Bloqueado: Debe confirmar el correo electronico"

        # Verificamos que la contraseña no este vacia
        if len(self.contrasena_plana.strip()) == 0:

            # Mostramos una laerta indicando que la contraseña es obligatoria
            return False, "[ALERTA] Bloqueado: La contraseña es obligatoria"

        # Verificamos que el usuario haya confirmado la contraseña
        if len(self.confirmar_contrasena.strip()) == 0:

            # Mostramos una alerta si no se confirmo la contraseña
            return False, "[ALERTA] Bloqueado: Debe confirmar la contraseña"

        # Verificamos si el usuario acepto
        # los terminos y condicionales
        # "not" significa "no"
        # Entonces:
            # - Si el valor es False = entra en la condicion
            # - Si es True = contiua normalmente
        if not self.aceptacion_terminos:

            # Mostramos un mensaje indicando
            # que debe acpetar los terminos antes de continuar
            return False, "[ALERTA] Bloquedado: Debe aceptar los terminos y condiciones"

        # Si todas las validaciones fueron correctas
        # devolvemos:
            # - True = indicando que todo esta valido
            # - None = porque no existe  ningun mensaje de error
        return True, None

    # Definimos el metodo "validar_formato_correo"
    # Su funcion es verificar que el correo electronico
    # tenga un formato basico valido
    # En este caso, comprobamos que el texto contenga el simbolo "@"
    def validar_formato_correo(self):

        # Verificamos que el campo
        # "correo_electronico" tenga algun contenido
        # Luego comprobamos que el simbolo "@"
        # este presente dentro del correo
            # "not in" significa: "no se encuentra dentro de"
        if self.correo_electronico and "@" not in self.correo_electronico:

            # Si el correo no contiene "@", devolvemos:
                # - False: indicando que la validacion fallo
                # - Un mensaje explicando el error
            return False, "[ALERTA] Bloqueado: Ingrese un correo electronico valido"

        # Si el correo cumple la validacion, devolvemos:
            # - True: Indicando que el formato es valido
            # - None: porque no existe ningun error
        return True, None

    # Definimos el metodo "validar_concidencia"
    # Su funcion es comprobar que los datos
    # ingresados dos veces por el usuario sean exactamente iguales
    # Esto ayuda a evitar errores de escritura
    # en el correo electronico y la contraseña
    def validar_coincidencia(self):

        # Comparamos el correo principal
        # con el coreo de confirmacion
        # "!=" sifnifica "diferente de"
            # Si ambos textos no coinciden, la validacion falla
        if self.correo_electronico != self.confirmar_correo:

            # Retornamos:
                # - False: indicando que ocurrio error
                # - Un mensajeinformando que los correos electronicos no coinciden
            return False, "[ALERTA] Bloqueado: Los correos electronicos no coinciden"

        # Comparamos la contraseña original
        # con la contraseña de confirmacion
        # Si los textos son diferentes
        # significa que el usuario cometio un error al escribirlas
        if self.contrasena_plana != self.confirmar_contrasena:

            # Mostramos un mensaje indicando que las contraseñas no coincidan
            return False, "[ALERTA] Bloqueado: Las contraseñas no coinciden"

        # Si ambas comparaciones fueron correctas,
        # devolvemos:
            # - True: indicando que los datos coinciden
            # - None: porque no existe ningun error
        return True, None

    # Definimos el metodo "validar_lon_contrasena"
    # Su objetivo es verificar que la contraseñ
    # tenga una longitud minima segura
    # Esto ayuda a mejorar la seguridad del sistema,
    # evitando contraseñas demasiado cortas y faciles de adivinar
    def validar_long_contrasena(self) :

        # "len()" cuenta la cantidad de caracteres
        # que tiene la contraseña ingresada
        # Si la longitud es menor a 8, la validacion falla
        if len(self.contrasena_plana) < 8:

            # Retornamos:
                # - False: indicando que la contraseña no cumple
                #   el requisito minimo de seguridad
                # - Un mensaje explicando el problema encontrado
            return False, "[ALERTA] Bloqueado: La contraseña debe tener al menos 8 caracteres"

        # Si la contraseña tiene 8 o mas caracteres,
        # devolvemos:
            # -True: indicando que la validacion fue exitosa
            # - None: porque no existe ningun error
        return True, None

    # --- SECCION 3: INTERACCION CON BASE DE DATOS --------------

    # Definimos el metodo "validar_unicidad_correo"
    # su funcion es verificar si el correo electronico
    # ya se encuentra registrado en la base de datos
    # Esto evita que existan usuarios duplicados con el ismo correo
    def validar_unicidad_correo(self) :

        # Importamos la funcion #obtener_conexion
        # desde el modulo de conexion
        # Esta funcion se encarga de crear
        # la conexion con la base de daos SQLite
        # La importacion se realiza dentro del metodo
        # para evitar problemas de importacion circular
        from database.conexion import obtener_conexion

        # Creamos una conexion activa con la base de datos
        conexion = obtener_conexion ()

        # Inicializamos la variable "existe" en False
        # Esto significa que, por defecto,
        # asumimos que el correo NO esta registrado
        # Mas adelante cambiara a True
        # si encontramos el correo en la base de datos
        existe = False

        # Iniciamos un bloque "try"
        # para ejecutar operaciones de base de datos
        # y poder manejar posibles errores
        try:

            # Creamos un cursor
            # El cursor es objeto que permite
            # ejecutar instrucciones SQL dentro de la base de datos
            # Si la conexion es el puente que te une a la base de datos, el cursor es el
            #  vehiculo que viaja por ese puente para llevar y traer la informacion
            cursor = conexion.cursor()

            # Ejecutamos una consulta SQL
            # para buscar un usuario con el mismo correo elctronico
            # "SELECT id" busca unicamente el identificador del usuario
            # El signo "?" funciona como marcador de posicion dentro de la consulta SQL
            # En el lugar de escribir directamente el valor del correo
            # dentro del texto SQL, lo enviamos por separado
            # como un parametro seguro
            # Python reeemplaza automaticamente el "?"
            # por el valor de "self.correo_electronico" al ejecutar la consulta
            # Esto es impotante porque: 
                # - Evita errores de escritura en consultas SQL
                # - Protege la base de datos contra ataques de inyeccion SQL
            cursor.execute("SELECT id FROM usuarios WHERE correo_electronico = ?", (self.correo_electronico,))

            # "fetchone()" obtiene el primer resultado encontrado de la consulta SQL
            # Si no existe ningun registro, el resultado sera None
            resultado = cursor.fetchone()

            # Verificamos si la consulta encontro
            #algun usuario con ese correo
            # Si "resultado" contiene informacion,
            # significa que el correo ya existe
            if resultado:

                # Cambiamos la variable "existe" a True
                # para indicar que el correo ya esta registrado
                existe = True

        # Capturamos cualquier error relacionado
        # con SQLite para evitar que el programa falle
        except sqlite3.Error as error_db:

            # Mostramos un mensaje de error en consola
            # si ocurre un problema durante la consulta SQL
            # La "f" antes de las comillas indica que estamso usando una f-string
            # (cadena formateada de Python)
            # Esto permmite insertar variables directamente
            # dentro del texto usando llaves { }
            # En este caso:
                # "{error_db}" sera reemplazado automaticamente por el detalle real del error ocurrido
                # Ejemplo: Error al verificar correo: no such table: usuarios
            print(f" # Error al verificar correo: {error_db} ")

        # El bloqueo "finally" se ejecuta siempre, exista o no un error
        # Aqui cerramos la conexion con la base de datos para liberar recursos del sistema
        finally:

            # Cerramos la conexion activa con la base de datos
            conexion.close()

        # Devolvemos el valor de la variable "existe"
            # - True: el correo ya esta registrado
            # - False: el correo todavia no existe
        return existe

    # Definimos el metodo el metodo "registrar_usuario"
    # Su funcion es guardar un nuevo usuario en la base de datos SQLite
    # Aqui tambien se aplican medidas de seguridad, como el cifrado de la contraseña
    def registrar_usuario(self):

        # Importamos la funcion "obtener_conexion"
        # para crear la conexion con la base de datos
        # La importacion se hace dentro del metodo para evitar importaciones circulares
        from database.conexion import obtener_conexion

        # Convertimos la contrasela escrita por el usuario en un jhash seguro
        # Un hash es una version cifrada e irreversible de la contraseña original
        # Esto protege la informacion del usuario, ya que nunca se guarda la contraseña real
        # en la base de datos
        hash_seguro = generate_password_hash(self.contrasena_plana)

        # Convertimos el valor de aceptacion de terminos
        # a 1 (verdadero) para almacenarlo en SQLite
        # En muchas bases de dtos:
            # - 1 representa True
            # - 0 representa False
        self.aceptacion_terminos = 1

        # Creamos una conexion activa con la base de datos
        conexion = obtener_conexion()

        # Inicializamos la variable "exito" en False
        # Esto significa que, inicialmente, asumimos que el registro aun no fue exitoso
        # Mas adelante cambiara a True si el usuario se guarda correctamente
        exito = False

        # Iniciamos un bloque "try" para manejar posibles errores
        # durante el proceso de insercion
        try:

            # Creamos un cursor para ejecutar instrucciones SQL
            cursor = conexion.cursor()

            # "cursor.execute()" se utiliza para enviar
            # instrucciones SQL a la base de datos
            # En este caso estamos ejecutando una consulta
            # de tipo "INSERT INTO", cuya funcion es agregar un nuevo registro en la tabla "usuarios"

            # Escribimos la instruccion SQL entre comillas triples (´´´ ´´´)
            # Las comillas triples permiten escribir consultas largas
            # En varias lineas para el codigo sea mas organizado y facil de leer

            # "VALUES" indica los datos que seran almacenados en cada columna de la tabla
            # Los signos "?" funcionan como marcadores de posicion
            # Python reemplaza automaticamente cada "?" por los valores enviados mas abajo
            # El valor "ACTIVO" esta escrito directamente,
            # por lo que todos inicialmente con ese estado
            # se registraran inicialmente con ese estado

            # Aqui enviamos la informacion real que reemplazara cada marcador "?"
            # El orden de los datos debe coincidir exactamente
            # con el orden de las columnas y los signos "?"

            # Relacion entre ada "?" y los datos enviados:
                # Primer ?:self.nombre_copleto
                # Segundo ?:self.correo_electronico
                # Tercer ?:hash_seguro
                # Cuarto ?:self.rol
                # Quinto ?:self.aceptacion_terminos
            # Esto permite innsertar los datos de manera segura
            # y organizada en la base de datos
            cursor.execute('''
                INSERT INTO usuarios (nombre_completo, correo_electronico,
                contrasena_hash, rol, estado, aceptacion_terminos)
                VALUES (?, ?, ?, ?, "ACTIVO", ?)''',
                (self.nombre_completo, self.correo_electronico, hash_seguro, self.rol, self.aceptacion_terminos))

            # Guardamos permanentemente los cambios
            # realizados en la base de datos
            # Sin "commit()", el nuevo usuario no quedaria almacenado
            conexion.commit()

            # Indicamos que el registro del usuario fue exitoso
            exito = True

        # Capturamos cualquier error relacionado con SQLite durante el proceso de insercion
        except sqlite3.Error as error_db:

            # Mostramos en consola el detalle del error ocurrido
            # La f-string permite insertar automaticamente
            # el contenido de la variabel "error_db" dentro del mensaje
            print(f"# Error al insertar usuario: {error_db}")

        # El bloque "finally" se ejecuta siempre, ocurra o no un error
        # Aqui cerramos la conexion para liberar rescursos
        finally:

            # Cerramos la cocnexion activa con la base de datos
            conexion.close()

        # Devolvemos el valor de la variable "exito"
            # - True: el usuario fue registrado correctamente
            # - False: ocurrio un error durante el registro
        return exito