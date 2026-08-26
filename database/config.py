# =====================================================

# config.py
# -----------------------------------------------------
# Modulo de configuracion global del sistema

# Este archivo centraliza las rutas utilizadas por la aplicacion,
# permitiendo que cualquier modulo pueda acceder a archivos criticos
# (como la base de datos o scripts SQL) desde una unica fuente

# Ventjas:
# - Evita rutas hardcodeadas
# - Facilita el mantenimiento del proyecto
# . Permite mover la aplicacion entre equipos sin modificar codigo
# - Mejora la organizacion y escabilidad

# Proyecto: PMV Plataforma Legal LEGALIS - SENA ADSO

# Autor: Equipo de desarrollo

# Verson: 1.0

# =============================================================

# Importemos la libreria "os" para poder interactuar con el sistema operativo.
# Permite realizar tareas comunes como leer carpetas, crear archivos, buscar rutas y ejecutar comandos del sistema
# sin importar el sistema operativo (Windows, Mac o Linux)
import os

# --- SECCION 1: RUTAS DE ARCHIVOS -------------
# Obtenemos la ruta de la carpeta donde se encuentra este archivo Python
# "_file_" representa el archivo actual y "os.path.dirname()"
# devuelve unicamente la carpeta que lo contiene
# Resultado: H:\Mi unidad\Plataforma_Lega\database
CARPETA_ACTUAL = os.path.dirname(__file__)
print(CARPETA_ACTUAL)

# Construimos la ruta completa de la base de datos
# "os.path.join()" une partes de una ruta de forma segura
# para que funcione correctamente en cualquier sistema operativo
# Resultado: H:\Mi unidad\Plataforma_Legal\database\plataforma_legal.db
RUTA_BD = os.path.join(CARPETA_ACTUAL, "plataforma_legal.db")
print(RUTA_BD)

# Creamos la ruta completa del archivo "schema.sql",
# el cual normalmente contiene las instrucciones SQL
# necesaria para crear las tablas y estructura de la base de datos
# Resultado: H:\Mi unidad\Plataforma_Legal\database\schema.sql
RUTA_SCHEMA = os.path.join(CARPETA_ACTUAL, "schema.sql")
print (RUTA_SCHEMA)

# =================================================================
# NOTA PARA EL APRENDIZ:
# Centralizar estos datos evita errores de rutas al mover el proyecto de carpeta
# =================================================================