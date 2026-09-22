// =======================================================
// ARCHIVO:    registro_validaciones.js
// FUNCION:    Validaciones del lado del cliente para formulario
// PROYECTO:   PMV Plataforma Legal - SENA ADSO
// VERSION:    2.0 (Optimizado y Facil)
// =======================================================

// -- SECCION 1: CONTROLADOR DE EVENTOS -------------

// document:    objeto global del navegador que representa el documento
//              HTML cagado en la pagina y proporciona metodos para
//              acceder y manipular sus elementos.
// addEventListener (): Metodo del objeto document utilizado para
//                      registrar un controlador de eventos (event listener)
//                      Permite ejecutar una funcion cuando ocurre el
//                      evento especificado.
// "DOMContentLoaded": Evento que se disparara cuando el navegador ha
//                     terminado de analizar (parsear) el documento HTML
//                     y el DOM ya esta construido, sin necesidad de
//                     esperar a que terminen de cargar imagenes,
//                     hojas de estilo u otros recursos externos.
// function(): Funcion anonima que se ejecutara automaticamente cuando
//             ocurra el evento "DOMContentLoaded".
// (): Indica que la funcion no recibe parametros directamente.
// La instruccion registra un evento para ejecutar la funcion unicamente
// cuando el DOM de la pagina haya sido completamente construido.
document.addEventListener("DOMContentLoaded", function() {

    // const: Palabra reservada de JavaScrip utilizada para declarar
    // una variable cuyo valor no puede ser reasignado despues de su inicializacion.
    // formulario: Nombre de la constante que almacenara la referencia
    //             al elemento HTML correspondiente al formulario.
    // document: Objeto global del navegador que representa el documento
    //           HTML actual y permite acceder a sus elementos.
    // getElementById(): Metodo del objeto document que busca y devuelve
    // el elemento HTML cuyo atributo "id" coincide con el valor proporcionado
    // "formulario-registro": Cadena de texto que contiene el identificador
    // (id) del formulario que se desea localizar.
    // La instruccion busca en el DOM el elemento cuyo id es
    // "formulario-registro y almacena su referencia en la constante "formulario".
    const formulario = document.getElementById("formulario-registro");

    // formulario: Referencia al elemento HTML del formulario obtenida
    //             prevenidamente mediante document.getElementById().
    //
    // addEventListener(): Metodo de JavaScript que registra un
    //                     controlador de eventos para ejecutar una
    //                     funcion cuando ocurre un evento especifico.
    //
    // "submit": Evento que se produce cuando el formulario intenta
    //           ser enviado, por ejemplo. al pulsar el boton "Registrarse".
    //
    // function(evento) : Funcion caliback que sera ejecutada cuando
    //                    ocurra el evento "submit".
    // evento: Parametro que recibe el objeto Event generado por el
    //         navegador y que contiene informacion sobre el evento.
    // La instruccion registra un controlador para interceptar el
    // envio del formulario y ejecutar primero las validaciones
    // definidas en JavaScript.
    formulario.addEventListener("submit",function(evento) {

        // evento: Objeto Event recibido por la funcion callback
        // preventDefault(): Metodo del objeto Event que cancela el
        //                   comportamiento predeterminado asociado al evento.
        //
        // En un formulario HTML, el comportamiento predeterminado del
        // evento "submit" es enviar los datos al servidor y recargar o
        // cambiar la pagina.
        // La instruccion cancela temporalmente ese comportamiento para
        // permitir que JavaScript ejecute las validaciones antes de enviar los datos.
        evento.preventDefault();

        // limpiarErrores(): Funcion definida en el mismo archivo JavaScript.
        //                   Su funcion es eliminar los mensajes de error
        //                   y las clases visuales de error generadas
        //                   durante una validacion anterior.
        // La instruccion ejecuta la limpieza de errores antes de iniciar
        // una nueva validacion del formulario.
        limpiarErrores();

        // let: Palabra reservada de JavaScript utilizada para declarar
        //      una variable cuyo valor puede modificarse posteriormente.
        // esValido: Variable utilizada como indicador general del estado
        //           de validacion del formulario.
        // true: Valor  booleano qie representa inicialmente un estado valido.
        // La instruccion inicializa el indicador suponiendo que el
        // formulario es valido hasta que alguna validacion determine lo contrario.
        let esValido = true;

        // validarObligatorios() : Funcion que verifica que los campos
        //                         obligatorios contengan informacion.
        // !: Operador logico NOT que invierte el valor booleano retornado.
        // Si la funcion retorna true, !true produce false.
        // Si retorna false, !false produce true
        // esValido = false: Cambia el indicador general a invalido
        // La instruccion ejecuta la validacion de campos obligatorios
        // y marca el formulario como invalido si dicha validacion falla.
        if (!validarObligatorios()) esValido = false;

        // validarFormatoCorreo() : Funcion que verifica que el correo
        //                          electronico tenga un formato valido.
        // La instruccion ejecuta la validacion del correo y establce
        // esValido en false si la validacion no es superada.
        if (!validarFormatoCorreo()) esValido = false;

        // validarCoincidencias() : Funcion que compara el correo con su
        //                          confirmacion y la contraseña con su confirmacion.
        // La instruccion establece esValido en false si alguna de las
        // comparaciones falla.
        if (!validarCoincidencias()) esValido = false;

        // validarSeguridadClave() : Funcion que verifica el requisito
        //                           minimo de longitud de la contraseña.
        // La instruccion establece esValido en false cuando la
        // contraseña no cumple dicha validacion.
        if (!validarSeguridadClave()) esValido = false;

        // validarTerminos() : Funcion que verifica si el usuario marco
        //                     la casilla de aceptacion de terminos.
        // La instruccion establece esValido en false si los terminos
        // no fueron aceptados.
        if (!validarTerminos()) esValido = false;

        // esValido: Variable booleana que contiene el resultado final
        //           de todas las validaciones ejecutadas anteriormente.
        // La condicion verifica si el valor permanece en true.
        // Si alguna validacion fallo, esValido habra cambiado a false
        // y este bloque no se ejecutara.
        if (esValido) {

            // formulario.submit() : Metodo del objeto HTMLFormElement
            //                       que envia manualmente el formulario.
            // A diferencia del evento "submit" capturado anteriormente,
            // esta llamada permite realizar el envio despues de que
            // las validaciones JavaScript hayan sido superadas.
            // La instruccion envia finalmente los datos del formulario
            // hacia la ruta definida en su atributo "action".
            formulario.submit();
        }
    // Finaliza la funcion callback asociada al evento "submit".
    });

    // -- Seccion 2: FUNCIONES DE LOGICA (VALIDACIONES) ------

    // function: Palabra reservada de JavaScript utilizada para
    //           declarar una funcion.
    // validarObligatorios: Nombre de la funcion encargada de verificar
    //                      que los campos definidos como obligatorios
    //                      contengan informacion.
    // (): Indica que la funcion no recibe parametros directamente.
    // La istruccion define la funcion que realizara la validacion
    // de los campos obligatorios del formulario.
    function validarObligatorios() {

        // let: Palabra reservada utilizada para declarar un variable
        //      cuyo valor puede modificarse posteriormente.
        // ok: Variable booleana utilizada como indicador del resultado
        //     general de la validacion.
        // true: Valor booleano que representa inicialmente una
        //       validacion correcta.
        // La variable se inicializa en true y cambiara a false si
        // alguno de los campos obligatorios no cumple la validacion
        let ok = true;

        // const: Palabra reservada utilizada para declarar una constante
        //        cuyo valor no puede se reasignado.
        // campos: Constante que almacena un arreglo (Array) de cadenas
        //         de texto con los identificadores HTML de los campos
        //         que seran sometidos a validacio.
        // []: Sintaxis utilizada en JavaScript para crear un arreglo.
        // Cada cadena corresponde al atributo "id" de un elemento HTML.
        // La instruccion define la coleccion de campos que la funcion debe revisar
        const  campos = ["nombre_completo", "correo_electronico", "confirmar_correo", "contrasena", "confirmar_contrasena"];

        // forEach(): Metodo de los arreglos de JavaScript utilizado para
        //            recorrer cada elemento de la coleccion y ejecutar
        //            una funcion una vez por cada elemento.
        // id: Parametro de la funcion flecha que recibe el valor del
        //     elemento actual del arreglo.
        // =>: Operador utilizado para definir una funcion flecha
        //     (Arrow Function)
        // La instruccion recorre todos los identificadores almacenados
        // en el arreglo "campos" y ejecuta el bloque de codigo para
        // cada uno de ellos.
        campos.forEach(id => {

            // const: Declara una constante cuyo valor no puede reasignarse
            // input: Varibale que almacenara la referencia al elemento
            //        HTML correspondiente al identificador actual.
            // document.getElementById(): Metodo que busca en el DOM
            //                            un elemento cuyo atributo "id"
            //                            coincida con el valor recibido.
            // id: Identificador del campo que se esta procesando
            // La instruccion obtine del DOM el elemento HTML asociado
            // al campo actual y almacena su referencia en "input".
            const input = document.getElementById(id);

            // if: Estructura condicional utilizada para ejecutar un bloque
            //     cuando una expresion booleana resulta verdadera.
            // value: Propiedad del elemento HTML utilizada para obtener
            //        el contenido actualmente introducido  en el campo
            // trim(): Metodo de las cadenas de JavaScript que elimina
            //         espacios en blanco al inicio y al final del texto
            // ===: Operador de comparacion estricta. Compara valor y tipo.
            // "": Cadena vacia utilizada para representar ausencia de
            //     contenido en el campo.
            // La instruccion verifica si el campo esta vacio despues de
            // eliminar espacios en blanco al inicio y al final.
            if (input.value.trim() === "") {

                // mostrarError(): Funcion definida en el mismo archivo
                //                 encargada de mostrar visualmente un
                //                 mensaje de error asociado al campo
                // id: Identificador del campo que presento el error
                // "Este campo no puede quedar vacio": Mensaje que sera
                // mostrado al usuario
                // La instruccion genera el mensaje de error en la
                // interfaz y aplica el estado visual correspondiente
                // al campo que esta vacio
                mostrarError(id, "Este campo no puede estar vacio");

                // ok: Variable que almacena el estado general de validacion
                // false: Valor booleano que indica que la validacion no fue superada
                // La instruccion cambia el indicador general a false
                // porque se encontro al menos un campo obligatorio vacio
                ok = false;
            }
        });

        // return: Palabra reservada de JavaScript utilizada para
        //         finalizar la ejecucion de la funcion y devolver
        //         un valor al codigo que realizo la llamada
        // ok: Contiene el resultado final de la validacion
        // La instruccion devuelve true cuando todos los campos
        // obligatorios contiene informacion y false cuando al menos
        // uno de ellos esta vacio
        return ok;
    }

    // Proposito: Validar que el correo tenga estructura de e-mail (usuario@dominio.com)
    // function: Palabra reservada de JavaScript utilizada para declarar una funcion
    // validarFormatoCorreo: Nombre de la funcion de
    //                       verificar que el correo electronico
    //                       tenga una estructura valida
    // (): Indica que la funcion no recibe parametros directamente
    // La instruccion define la funcion que realizara la validacion
    // del formato del correo electronico.
    function validarFormatoCorreo() {

        // const: Palabra reservada utilizada para declarar una constante
        //        cuyo valor no puede ser reasignado
        // correo: Constante que almacena la referencia al elemento HTML
        //         correspondiente al campo de correo electronico
        // document.getElementById(): Metodo del objeto document que
        //                            busca en el DOM un elemento cuyo
        //                            atributo "id" coincida con el valor
        //                            proporcionado
        // "correo_electronico": Identificador HTML del campo que contiene
        //                       el correo electronico
        // La instruccion obtiene del DOM el elemento input correspondiente
        // al campo de correo y almacena su referencia en "correo"
        const correo = document.getElementById("correo_electronico");

        // Expresion regular: el "molde" que debe seguir un correo
        // const: Declara una constante
        // patron: Variable que almacena una expresion regular (RegExp)
        // /.../: Sintaxis utilizada en JavaScript para definir una expresion regular
        // ^: Indica el inicio de la cadena
        // [^\s@]+: Exige uno o mas caracteres que no sean espacios
        //          en blanco ni el caracter "@"
        // @: Exige la presencia del caracter "@"
        // [^\s@]+: Exige uno o mas caracteres despues del @, evitando
        //          nuevamente espacios y otro @
        // \.: Exige la presencia de un punto literal "."
        // [^\s@]: Exige uno o mas caracteres despues del punto
        // $: Indica el final de la cadena
        // La expresion regular define el patron basico que debe cumplir
        // el texto para ser considerado un correo electronico valido.
        const patron = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // if: Estructura condicional que ejecuta un bloque cuando la
        //     expresion evaluada resulta verdadera
        // correo.value: Propiedad que contiene el valor actualmente
        //               introducido en el campo HTML
        // trim(): Metodo de las cadenas de texto que elimina espacios
        //         en blanco al inicio y al final
        // !==: Operador de comparacion estricta que verifica que dos
        //      valores no sean iguales
        // "": Cadena vacia utilizada para representar ausencia de texto
        // &&: Operador logico AND. Requiere que ambas condiciones sean
        //     verdaderas para que el resultado completo sea true
        // !: Operador logico NOT que invierte el resultado booleano
        // patron.test (): Metodo de una expresion regular que comprueba
        //                 si una cadena coincide con el patron definido
        // correo.value: Valor original del campo que sera evaluado
        // La condicion comprueba dos sistuaciones:
            // 1. Que el campo no este vacio
            // 2. Que el valor ingresado no coincida con la expresion regular
        // Si ambas condiciones son verdaderas, el correo se considera
        // invalido y se ejecuta el bloque condicional
        if (correo.value.trim() !== "" && !patron.test(correo.value)) {

            // mostrarError(): Funcion definida en el mismo archivo
            //                 utilizada para mostrar visualmente un
            //                 mensaje asociado al campo que presento
            //                 la validacion incorrecta.
            // "correo_electronico": Identificador del campo HTML donde
            //                       se produjo el error
            // "El correo no tiene un formato valido": Texto que sera
            //                                         mostrado al usuario
            // La instruccion envia a mostrarError() el identificador
            // del campo y el mensaje que debe presentarse
            mostrarError('correo_electronico', "El correo no tiene formato valido");
            return false;
        }

        // return: Palabra reserrvada de JavaScript que finaliza la
        //         ejecucion de la funcion y devuelve un valor
        // false: Valor booleano que indica que la validacion fallo
        // La instruccion termina la funcion e informa al codigo que
        // la llamo que el correo no supero la validacion
        return true;
    }

    // Proposito: Asegurar que el usuario no se equivoque al repetir datos
    // function: Palabra reservada de JavaScript utilizada para
    //           declarar una funcion
    // validarCoincidencias: Nombre de la funcion encargada de comprobar
    //                       que los valores de confirmacion coincidan
    //                       con los valores originales.
    // (): Indica que la funcion no recibe parametros directamente
    // La instruccion define la funcion encargada de validar la
    // coincidencia entre el correo electronico y su confirmacion,
    // y entre la contraseña y su confirmacion
    function validarCoincidencias() {

        // let: Palabra reservada utilizada para declarar una variable
        //      cuyo valor puede modificarse posteriormente
        // ok: Variable booleana utilizada para almacenar el resultado
        //     general de las validaciones realizadas por la funcion
        // true: Valor inicial que indica que, hasta ese momento, no
        //       se ha detectado ninguna diferencia
        let ok = true;

        // const: Palabra reservada utilizada para declarar una constante
        // c1: Constante que almacena el valor actual del campo principal
        //     del correo electronico
        // document.getElementById(): Metodo que localiza en el DOM el
        //                            elemento cuyo id coincide con el valor indicado
        // "correo_electronico": Identificador del campo principal del correo
        // value: Propiedad que contiene el valor ingresado actualmente
        //        en el elemento HTML
        // La instruccion obtiene el valor del correo electronico principal
        const c1 = document.getElementById('correo_electronico').value;

        // c2: Constante que almacena el valor actual del campo utilizado
        //     para confirmar el correo electronico
        // La instruccion obtiene el valor introducido en el segundo
        // campo de correo
        const c2 = document.getElementById('confirmar_correo').value;

        // p1: Constante que almacena el valor actual del campo principal
        //     de contraseña
        // La instruccion obtiene la contraseña introducida inicialmente
        const p1 = document.getElementById('contrasena').value;

        // p2: Constante que almacena el valor actual del campo utilizado
        //     para confirmar la contraseña
        // La instruccion obtiene la contraseña introducida en el campo
        // de confirmacion
        const p2 = document.getElementById('confirmar_contrasena').value;

        // if: Estructura condicional que ejecuta un bloque cuando la
        //     expresion evaluada resulta verdadera
        // c2 !== "": Operador de comparacion estricta que verifica que
        //            el campo de confirmacion no este vacio
        // &&: Operador logico AND que exige que ambas condiciones sean verdaderas
        // c1 !== c2: Compara estrictamentte el correo principal con el
        //            correo de confirmacion
        // La condicion verifica que exista un valor en el campo de
        // confirmacion y que dicho valorsea diferente al correo principal
        if (c2 !== "" && c1 !== c2) {

            // motrarError(): Funcion definida en el mismo archivo que
            //                muestra un mensaje de error asociado a un campo especifico
            // "confirmar_correo": Identificador del campo donde se
            //                     decteto la diferencia
            // Mensaje: Texto que informa al usuario que los correos
            //          electronicos no coinciden
            // La instruccion muestra el error directamente sobre el
            // campo de confirmacion del correo
            mostrarError('confirmar_correo', "Los correo electronicos no coinciden");

            // ok: Variable que contiene el estado general de validacion
            // false: Valor booleano que indica que se decteto un error
            // La instruccion marca la validacion general como incorrecta
            ok = false;
        }

        // if: Segunda estructura condicional independiente
        // p2 !== "": Verifica que el campo de confirmacion de contraseña
        //            no este vacio
        // p1 !== p2: Compara la contraseña principal con la contraseña de confirmacion
        // La condicion verifica que exista una contraseña de confirmacion
        // y que ambas contraseñas sean diferentes
        if (p2 !== "" && p1 !== p2) {

            // mostrarError(): Funcion que muestra el mensaje visual
            //                 associado al campo que presenta el error
            // "confirmar_contraseña": Identificador del campo de
            //                          confirmacion de contraseña
            // Mensaje: Texto mostrado al usuario cuando las contraseñas no coinciden
            mostrarError('confirmar_contrasena', "Las contraseñas no coinciden");

            // ok= false: Cambia el estado general de la validacion
            //            para indicar que existe un error
            ok = false;
        }

        // return: Palabra reservada de JavaScript utilizada para
        //         finalizar la funcion y devolver un valor
        // ok: Contiene el resultado final de ambas comprobaciones
        // true: Los valores coinciden correctamente
        // false: Al menos una de las comparaciones detecto una diferencia
        // La instruccion devuelve el resultado general de la validacion
        return ok;
    }

    // Proposito: Exigir un minimo de 8 caracteres por seguridad
    // function: Palabra reservada de JavaScript utilizaa para declarar una funcion
    // validarSeguridadClave: Nombre de la funcion encargada de
    //                        verificar que la contraseña cumpla con
    //                        la longitud minima establecida
    // (): Indica que la funcion no recibe parametros directamente
    // La instruccion define la funcion que valida el requisito
    // minimo de longitud de la contraseña
    function validarSeguridadClave() {

        // const: Palabra reservada utilizada para declarar una constante
        //        cuyo valor no puede se reasignado
        // clave: Constante que almacena la referencia al elemento HTML
        //        correspondiente al campo de contraseña
        // document.getElementById(): Metodo del objeto document que
        //                            busca en el DOM un elemento cuyo
        //                            atributo "id" coincida con el valor proporcionado
        // "contraseña": Identificador HTML del campo de contraseña
        // La instruccion localiza el campo de contraseña en el DOM y
        // almacena su referencia en la constante "clave"
        const clave = document.getElementById('contrasena')

        // if: Estructura condicional que ejecuta un bloque cuando la
        //     expresion evaluada resulta verdadera
        // clave.value: Propiedad que contiene el valor introducido
        //              actualmente en el campo de contraseña
        // trim(): Metodo de las cadenas de texto que elimina espacios
        //         en blanco all inicio y al final
        // !== "": Comprueba que el resultado no sea una cadena vacia
        // &&: Operador logico AND que exige que ambas condiciones sean verdaderas
        // length: Propiedad de una cadena que devuelve la cantidad
        //         de caracteres que contiene
        // <8: Operador de comparacion que verifica si la longitud
        //     de la contraseña es inferior a 8 caracteres
        // La condicion comprueba que la contraseña no este vacia y,
        // al mismo tiempo, que tenga menos de 8 caracteres
        if (clave.value.trim() !== "" && clave.value.length < 8) {

            // mostrarError(): Funcion definida en el mismo archivo
            //                 que muestra visualmente un mensaje de error
            //                 asociado al campo que presenta la validacio incorrecta
            // "contraseña": Identificador del campo donde se presenta el error
            // "La clave debe tener al menos 8 caracteres": Mensaje que
            //                          informa al usuario del registro
            // La instruccion muestra el mensaje de error sobre el campo de contraseña
            mostrarError('contrasena', "La clave debe tener al menos 8 caracteres")

            // return: Palabra reservada de JavaScript que finaliza
            //         la ejecucion de la funciony devuelve un valor
            // false: Valor booleano que indica que la validacion fallo
            // La instruccion termina la funcion e informa que la
            // contraseña no cumple con la longitud minima
            return false;
        }

        // return: Finaliza la ejecucion de la funcion y devuelve un valor booleano
        // true: Ondica que la contraseña supera esta validacion
        // Esta instruccion se ejecuta cuando la contraseña tiene
        // 8 o mas caracteres o cuando el campo este vacio, dejando
        // la validacion de obligatoriedad a la funcion correspondiente
        return true;
    }

    // Proposito: Verificar que se acepten los terminos legales (RF05)

    // function: Palabra reservada de JavaScript utilizada para declarar una funcion
    // ValidarTerminos: Nombre de la funcion encargada de verificar
    //                  que el usuario haya aceptado los terminos y
    //                  condiciones antes de continuar
    // (): Indica que la funcion no recibe parametros directamente
    // La instruccion define la funcion encargada de validar el
    // estado dek checkbox de acpetacion de terminos
    function validarTerminos() {

        // const: Palabra reservada utilizad para declarar una constante
        //        cuyo valor no puede ser reasignado
        // check: Constante que almacena la referencia al elemento HTML
        //        correspondiente a la casilla de aceptacion
        // document.getElementById(): Metodo del objeto document que
        //                            busca en el DOM un elemento cuyo
        //                            atributo "id" coincida con el valor proporcionado
        // "aceptacion_terminos": Identificador HTML asignado al checkbox
        // La instruccion localiza la casilla de acpetacion en el DOM y
        // almacena su referncia en la constante "check"
        const check = document.getElementById('aceptacion_terminos');

        // if: Estructura condicional que ejecuta un bloque cuando la
        //     condicion evaluada resulta verdadera
        // checked: Propiedad booleana de los elementos HTML de tipo
        //          checkbox que indica si la casilla esta selecionada
        //          - true: casilla marcada
        //          - false: casilla desmarcada
        // !: Operador logico NOT que invierte el valor booleano
        // !check.checked: Sera true cuando la casilla NO este marcada
        // La condicion verifica si el usuario no ha seleccionado la
        // casilla de aceptacion de terminos
        if (!check.checked) {

            // mostrarError(): Funcion definida en el mismo archivo
            //                 utilizada para mostrar visualmente un
            //                 mensasje de error asociado a un elemento
            // "aceptacion_terminos": Identificador del elemento HTML
            //                        donde se detecto el problema
            // "Debe aceptar los terminos para continuar": Mensaje que
            //                              se mostrara al usuario
            // La instruccion muestra el mensaje de validacion asociado
            // al checkbox cuando este no esta seleccionado
            mostrarError('aceptacion_terminos', "Debe aceptar los terminos para continuar");

            // return: Palabra reservada de JavaScript utilizada para
            //         finalizar la ejecucion de la funcion y devolver un valor
            // false: Valor booleano que indica que la validacion fallo
            // La instruccion termina la funcion y comunica al codigo
            // que la aceptacion de terminos no fue realizada
            return false;
        }


        // return: Finaliza la ejecucion de la funcion y devuelve
        //         un valor booleano
        // true: Indica que la condicion de aceptacion fue cumplida
        // La instruccion se ejcuta cuando el checkbox esta marcado
        return true;
    }

    // -- SECCION 3: AYUDANTES VISUALES (FRONTEND) ---------

    // Funcion que "dibuja" el error en la pantalla
    // function: Palabra reservada de JavaScript utilizada para
    //           declarar una funcion
    // mostrarError: Nombre de la funcion encargada de mostrar
    // visualmente un mensaje de error asociado a un elemento del formulario
    // id: Parametro que recibe el identificador HTML del elemento
    //     que presenta el error
    // mensaje: Parametro que recibe el texto que se mostrara al
    //          usuario como mensaje de validacion
    // La instrucción define una función reutilizable que recibe el
    // identificador del campo y el mensaje correspondiente para
    // presentar visualmente el error.
    function mostrarError(id, mensaje) {
        
        // const: Palabra reservada utilizada para declarar una constante.
        // span: Constante que almacenará la referencia al elemento HTML
        // destinado a mostrar el mensaje de error.
        // document.getElementById(): Método que busca en el DOM un
        // elemento cuyo atributo "id" coincida
        // con el valor proporcionado.
        // 'error-' + id: Operador + utilizado para concatenar cadenas.
        // Genera dinámicamente el identificador del
        // elemento donde se mostrará el error.
        // Por ejemplo, si id = "correo_electronico", el resultado será:
        // "error-correo_electronico".
        // La instrucción localiza el elemento HTML correspondiente al
        // mensaje de error y almacena su referencia en "span".
        const span = document.getElementById('error-' + id);

        // const: Declara una constante.
        // input: Constante que almacena la referencia al elemento HTML
        // que originó el error.
        // document.getElementById(id): Busca en el DOM el elemento cuyo
        // atributo "id" coincide con el parámetro.
        // La instrucción obtiene el campo que se está validando y
        // almacena su referencia en "input".
        const input = document.getElementById(id);

        // if: Estructura condicional.
        // span: Referencia al elemento destinado a mostrar el error.
        // En una condición, un objeto existente se evalúa como verdadero
        // (truthy), mientras que null se evalúa como falso.
        // La instrucción verifica si el elemento de mensaje de error
        // fue encontrado correctamente en el DOM.
        if (span) {

            // textContent: Propiedad que permite establecer o recuperar
            // el contenido de texto de un elemento HTML.
            // mensaje: Parámetro que contiene el texto del error.
            // La instrucción reemplaza el contenido del elemento span
            // por el mensaje recibido por la función.
            span.textContent = mensaje;
        
            // style: Propiedad que permite acceder directamente a los
            // estilos CSS en línea de un elemento HTML.
            // display: Propiedad CSS que controla si el elemento se
            // muestra u oculta.
            // 'block': Valor CSS que hace que el elemento se comporte
            // como un bloque y sea visible.
            // La instrucción hace visible el elemento que contiene el mensaje de error.
            span.style.display = 'block';
        }

            // if: Estructura condicional que comprueba si el elemento
            // asociado al campo fue encontrado correctamente.
            // input: Referencia al elemento HTML que presentó el error.
            // Si el elemento existe, la condición se evalúa como verdadera.
        if (input) {

                // classList: Propiedad que proporciona acceso a la lista
                // de clases CSS asociadas a un elemento HTML.
                // add(): Método que agrega una clase CSS al elemento.
                // 'input-error': Nombre de la clase CSS que se añade al
                // campo para aplicar el estilo visual
                // correspondiente al estado de error.
                // La instrucción añade la clase "input-error" al elemento
                // para identificarlo visualmente como un campo con error.
                input.classList.add('input-error'); // Pone el borde rojo
            }
        }

        // Función que limpia la pantalla para una nueva validación
        // function: Palabra reservada de JavaScript utilizada para declarar una función.
        // limpiarErrores: Nombre de la función encargada de eliminar
        // los mensajes y estilos visuales generados por
        // las validaciones anteriores.
        // (): Indica que la función no recibe parámetros directamente.
        // La instrucción define una función reutilizable que restablece
        // el estado visual del formulario antes de iniciar una nueva validación.
        function limpiarErrores() {

            // Buscamos todos los mensajes de error y los ocultamos
            // document: Objeto global del navegador que representa el
            // documento HTML actual.
            // querySelectorAll(): Método que permite localizar todos los
            // elementos del DOM que coincidan con un selector CSS determinado.
            // '.error-campo': Selector CSS que identifica todos los elementos
            // utilizados para mostrar mensajes de error.
            // La instrucción obtiene una colección con todos los elementos
            // que poseen la clase "error-campo".
            
            // forEach(): Método utilizado para recorrer cada elemento
            // de la colección obtenida por querySelectorAll().
            // s: Parámetro de la función flecha que representa el
            // elemento actual durante cada iteración.
            // =>: Sintaxis utilizada para definir una función flecha.
            // La instrucción ejecuta el bloque siguiente una vez por
            // cada mensaje de error encontrado.
            document.querySelectorAll('.error-campo').forEach(s => {

                // textContent: Propiedad utilizada para consultar o
                // modificar el contenido de texto de un
                // elemento HTML.
                // "": Cadena vacía.
                // La instrucción elimina el texto contenido actualmente
                // en el elemento que mostraba el mensaje de error.
                s.textContent = "";

                // style: Propiedad que permite acceder a los estilos
                // CSS aplicados directamente al elemento.
                // display: Propiedad CSS que controla la visualización
                // del elemento.
                // 'none': Valor CSS que oculta completamente el elemento.
                // La instrucción oculta el elemento utilizado para
                // mostrar el mensaje de error.
                s.style.display = 'none';
            });
            // Quitamos los bordes rojos de todos los inputs
            // document.querySelectorAll(): Busca nuevamente elementos en
            // el DOM utilizando un selector CSS.
            // '.input-campo': Selector que identifica los campos normales del formulario.
            // 'input[type="checkbox"]': Selector que identifica los elementos
            // input cuyo atributo type es checkbox.
            // ,: Permite combinar ambos selectores en una única búsqueda.
            // La instrucción obtiene todos los campos de entrada normales
            // y todas las casillas de verificación del formulario.

            // forEach(): Recorre cada elemento obtenido por
            // querySelectorAll().
            // i: Parámetro que representa el elemento actual de la
            // colección durante cada iteración.
            // La instrucción ejecuta el bloque para cada campo encontrado.
            document.querySelectorAll('.input-campo, input[type="checkbox"]').forEach(i => {

                // classList: Propiedad que proporciona acceso a la lista
                // de clases CSS asociadas al elemento.
                // remove(): Método que elimina una clase CSS del elemento.
                // 'input-error': Clase utilizada para identificar
                // visualmente un campo que presenta un error.
                // La instrucción elimina la clase "input-error" y devuelve
                // el campo a su estado visual normal.
                i.classList.remove('input-error');
            });
    }
});
