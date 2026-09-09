-- =======================================================================================
-- ARCHIVO:    schema.sql
-- FUNCION:    Script de creacion de la tabla de usuarios
-- PROYECTO:   PMV Plataforma Legal - SENA ADSO
-- VERSION:    1.0
-- =======================================================================================

--
-- Elemento: Sentencia de creacion de tabla "usuarios"
--
-- Comentario Tecnico:
    -- Instruccion que crea la tabla "usuarios" en la base de datos
    -- Sila tabla ya existe, no la vuelve a crear (evita errores)
--
-- Funcion Tecnica:
    -- Define una estructura para guardar informacion de usuarios
    -- Verifica si la tabla existe antes de crearla
--
-- Rol Arquitectonico:
    -- Base de almacenamiento de datos de usuarios dentro del sistema
--
-- Diccionario:
    -- - CREATE TABLE: comando para crear una tabla
    -- - IF NOT EXISTS: evita crear la tabla si ya esta creada
    -- - usuarios: nombre de la tabla donde se guardan los datos
--
CREATE TABLE IF NOT EXISTS usuarios (

    --
    -- Elemento: Campo "id" de la tabla usuarios
    --
    -- Comentario Tecnico:
        --Columna que identifica de forma unica a cada usuario
        -- Su valor se genera automaticamente y aumenta con cada nuevo registro
    --
    -- Funcion Tecnica:
        --Asignar un identificador unico a cada registro
        -- Evitar duplicados y permetir busquedas precisas
    --
    -- Rol Arquitectonico: Clave principal de la tabla (identificador unico del sistema)
    --
    -- Diccionario:
        -- - INTEGER: tipo de dato numerico
        -- - PRIMARY KEY: indica que es el identificador unico
        -- - AUTOINCREMENT: genera automaticamente el siguiente numero
    --
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    --
    -- Elemento: Campo "nombre_completo" de la tabla usuarios
    --
    -- Comenario Tecnico:
        -- Columna que almacena el nombre completo del usuario en formato texto
        -- Es un campo obligatorio, no puede quedar vacio
    --
    -- Funcion Tecnica: Guardar el nombre del usuario para su identificacion dentro del
    -- sistema
    --
    -- Rol arquitectonico: Dato basico de identificacion del usuario
    --
    -- Diccionario:
        -- - TEXT: tipo de dato para texto
        -- - NOT NULL: obliga a que el campo tenga un valor
    --
    nombre_completo TEXT NOT NULL,

    --
    -- Elemento: Campo "correo_electronico" de la tabla usuarios
    --
    -- Comentario Tecnico:
        -- Columna que almacena el correo electronico del usuario en formato texto
        -- Es obligatorio y no permite valores repetidos
    --
    -- Funcion Tecnica:
        -- Guardar el correo del usuario como daro de contacto y acceso
        -- Evitar que esxistan usuarios con el mismo correo
    --
    -- Rol arquitectonico: Identificador logico del usuario dentro del sistema (login)
    --
    -- Diccionario:
        -- - TEXT: Tipo de dato para texto
        -- - NOT NULL: obliga a que el campo tenga un valor
        -- - UNIQUE: no permite valores duplicados
    correo_electronico TEXT NOT NULL UNIQUE,

    --
    -- Elemento: Campo "contraseña_hash" de la tabla usuarios
    --
    -- Comentario Tecnico:
        -- Columnaque almacena la contraseña del usuario en formato cifrado (hash)
        -- Es un campo obligatorio
    --
    -- Funcion Tecnica:
        -- Guardar de forma segura la contraseña del usuario
        -- Permitir validar el acceso sin guardar la contraseña original
    --
    -- Rol arquitectonico: Mecanismo de autentificacion del sistema
    --
    -- Diccionario:
        -- - TEXT: tipo de dato para texto
        -- - NOT NULL: obliga a que el campo tenga un valor
        -- - hash: resultado de transformar la contraseña en un valor irreconocible
    --
    contrasena_hash TEXT NOT NULL,

    --
    -- Elemento: Campo "rol" de la tabla usuarios
    --
    -- Comentario tecnico:
        -- Columna que indica el tipo de usuario dentro del sistema
        -- Es obligatoria y, si no se especifica, toma por defecto el valor "Cliente"
    --
    -- Funcion tecnica: Definir que tipo de usuario es y que puede hacer dentro del sistema
    --
    -- Rol Arquitectonico: Control de acceso y permisos (define niveles dentro del sistema)
    --
    -- Diccionario:
        -- - TEXT: tipo de dato para texto
        -- - NOT NULL: obliga a que el campo tenga un valor
        -- - DEFAULT: asigna un valor automatico si no se envia uno
        -- - Cliente: rol basico por defecto
    --
    rol TEXT NOT NULL DEFAULT "Cliente",

    --
    -- Elemento: Campo "estado" de la tabla usuarios
    --
    -- Comentario tecnico:
        -- Columna que indica la situacion actual del usuario dentro del sistema
        -- Es obligatoria y, por defecto, se asigna como "Activo"
    --
    -- Funcion tecnica: Permitir activar o desactivar usuarios sin eliminarlos de la base de -- datoa
    --
    -- Rol Arquitectonico: Contorl de disponibilidad del usuario en el sistema
    --
    -- Diccionario:
        -- - TEXT: tipo de dato para texto
        -- - NOT NULL: obliga a qu el campo tenga un valor
        -- - DEFAULT: asigna un valor automatico si no se envia uno
        -- - Activo: usuario habilitado para usar el sistema
    --
    estado TEXT NOT NULL DEFAULT "Activo",

    --
    -- Elemento:
    -- Campo "aceptacion terminos" de la tabla usuarios
    --
    -- Comentario tecnico:
        -- Columna que indica si el usuario acepto los terminos y condiciones
        -- Se guarda como un valor numerico (0 = no, 1 = si)
        -- Es un campo obligatorio
    --
    -- Funcion Tecnica: Rgistrar si el usuario dio su aceptacion antes de usuar el sistema
    --
    -- Rol arquitectonico: Control de cumplimiento (verifica que el usuario acepto
    -- condiciones antes de acceder)
    --
    -- Diccionario:
        -- - INTEGER: tipo de dato numerico
        -- - NOT NULL: obliga a que el campo tenga un valor
        -- - 0: no acepto
        -- - 1: acpeto
        --
        aceptacion_terminos INTEGER NOT NULL

--
-- Elemento: Cierre de la sentencia de creacion de tabla
--
-- Comentario tecnico: Indica el final de la definicion de la tabla en la base de datos
--
-- Funcion Tecnica: Finalizar correctamente la instruccion CREATE TABLE para que sea
-- ejecutada sin errores
--
-- Rol arquitectonico: Delimitador de la estructura de la tbla dentro del sistema
--
-- Diccionario:
    -- - ): cierra la definicion de columnas
    -- - ;: finaliza la instruccion SQL
--
);
