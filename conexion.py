import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        # Intentar establecer la conexión
        conexion = mysql.connector.connect(
            host="autorack.proxy.rlwy.net",  # Usa la IP si el DNS falla
            user="root",
            password="sijpXgRGVhlXlEUXQuLQNMQOrdadHmGQ",
            database="railway",
            port=54237,
            connection_timeout=300
        )
        conexion = mysql.connector.connect(
            host="localhost",  # Usa la IP si el DNS falla
            user="root",
            password="",
            database="libros",
            port=3306,
            connection_timeout=300
        )
        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        # Manejo de errores específicos
        if e.errno == 1045:  # Error de autenticación
            print("Error: Credenciales incorrectas")
        elif e.errno == 1049:  # Base de datos desconocida
            print("Error: Base de datos no encontrada")
        elif e.errno == 2003:  # Error al conectar al servidor MySQL
            print("Error: No se puede conectar al servidor MySQL")
        else:
            # Otros errores
            print(f"Error inesperado: {e}")
    finally:
        # Mensaje en caso de fallo
        print("Intento de conexión finalizado.")
